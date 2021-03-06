import json
import os

from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, FormView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from GA import settings

from GA import settings
from .forms import DateReportForm, ProductReportForm, LocationReportForm, GeneralReportForm
from inventario.models import MoveIn, Move_Out, ProductClass, Product, User
from inventario.code_generator import *

class LandingPage(LoginRequiredMixin, TemplateView):
    template_name = 'reporte/home.html'
    login_url = reverse_lazy('inventario:login')

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
        return context


class DisposableProductView(LoginRequiredMixin, TemplateView):
    template_name = 'reporte/disposable/disposable_product.html'
    login_url = reverse_lazy('inventario:login')

    def get_context_data(self, **kwargs):
        context = super(DisposableProductView, self).get_context_data(**kwargs)
        movements = []
        for move in Move_Out.objects.all().order_by('-date'):
            if move.product_class.is_disposable or move.destiny == settings.LOCATIONS[4]:
                movements.append(move)


        context['movements'] = movements
        return context


class GeneralReportView(LoginRequiredMixin, FormView):
    form_class = GeneralReportForm
    template_name = 'reporte/general/general_form.html'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('reporte:home')

    @classmethod
    def currency_format(self, value):
        return "{:,.2f} Bs".format(value)

    def get_context_data(self, **kwargs):
        context = super(GeneralReportView, self).get_context_data(**kwargs)

        product_class = ProductClass.objects.all().order_by('name', 'product_type', 'size', 'brand')

        global_report = []
        general_value = 0
        wareHouse_value = 0
        office_value = 0
        polar_value = 0
        mante_value = 0
        disposable_value = 0

        for product in product_class:
            stock_almacen = Product.objects.filter(product_class=product, available=True, location=settings.LOCATIONS[0]).count()
            stock_oficina = Product.objects.filter(product_class=product, available=True, location=settings.LOCATIONS[1]).count()
            stock_planta = Product.objects.filter(product_class=product, available=True, location=settings.LOCATIONS[2]).count()
            stock_mante = Product.objects.filter(product_class=product, available=True, location=settings.LOCATIONS[3]).count()
            stock_desin = Product.objects.filter(product_class=product, available=False).count()

            setattr(product, 'stock_almacen', stock_almacen)
            setattr(product, 'stock_oficina', stock_oficina)
            setattr(product, 'stock_planta', stock_planta)
            setattr(product, 'stock_mante', stock_mante)
            setattr(product, 'stock_desin', stock_desin)
            setattr(product, 'product_value', GeneralReportView.currency_format((product.their_value * product.stock)))

            global_report.append(product)

            general_value += product.their_value * product.stock
            wareHouse_value += product.their_value * stock_almacen
            office_value += product.their_value * stock_oficina
            polar_value += product.their_value * stock_planta
            mante_value += product.their_value * stock_mante
            disposable_value += product.their_value * stock_desin

        context['global_report'] = global_report
        context['general_value'] = GeneralReportView.currency_format(general_value)
        context['wareHouse_value'] = GeneralReportView.currency_format(wareHouse_value)
        context['office_value'] = GeneralReportView.currency_format(office_value)
        context['polar_value'] = GeneralReportView.currency_format(polar_value)
        context['mante_value'] = GeneralReportView.currency_format(mante_value)
        context['disposable_value'] = GeneralReportView.currency_format(disposable_value)

        return context


class ProductReportView(LoginRequiredMixin, FormView):
    form_class = ProductReportForm
    template_name = 'reporte/product/product_form.html'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('reporte:product')

    def form_valid(self, form):
        product_class = form.cleaned_data['product_class']

        self.request.session['product_class'] = product_class
        return super(ProductReportView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductReportView, self).get_context_data(**kwargs)
        context['products'] = serializers.serialize(
            'json',
            ProductClass.objects.all().order_by('name', 'product_type', 'size', 'brand')
        )

        if 'product_class' in self.request.session:
            product_class = self.request.session['product_class']

            product = ProductClass.objects.get(pk=product_class)

            entrance = MoveIn.objects.filter(product_class=product_class, is_move_in=True).order_by('-date')
            movement = Move_Out.objects.filter(product_class=product_class).order_by('-date')

            product_report = True

            context['entrance'] = entrance
            context['movement'] = movement
            context['product_report'] = product_report

            del self.request.session['product_class']

        return context


class DateReportView(LoginRequiredMixin, FormView):
    form_class = DateReportForm
    template_name = 'reporte/date/date_form.html'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('reporte:date')


    def form_valid(self, form):
        init_date = form.cleaned_data['init_date']
        end_date = form.cleaned_data['end_date']
        location = form.cleaned_data['location']
        in_out = form.cleaned_data['in_out']

        end_date = datetime.strftime(
                    (datetime.strptime(end_date, "%Y-%m-%d")
                    + timedelta(days=1)), "%Y-%m-%d")

        self.request.session['location'] = location
        self.request.session['init_date'] = init_date
        self.request.session['end_date'] = end_date
        self.request.session['in_out'] = in_out

        return super(DateReportView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DateReportView, self).get_context_data(**kwargs)
        context['locations'] = settings.LOCATIONS
        movements = []

        #if there is any info on session do:
        if 'init_date' in self.request.session and 'end_date' in self.request.session and 'location' in self.request.session:
            init = self.request.session['init_date']
            end = self.request.session['end_date']
            status = self.request.session['in_out']
            location = self.request.session['location']

            context['status'] = status

            if status:
                if location == settings.LOCATIONS[0]:
                    movements = MoveIn.objects.filter(
                        date__gte=init,
                        date__lte=end,
                        is_move_in=True
                    ).order_by('-date')
                    context['date_report'] = movements
                else:
                    movements = Move_Out.objects.filter(
                        date__gte=init,
                        date__lte=end,
                        destiny=location
                    ).order_by('-date')
                    context['date_report'] = movements
            else:
                print(status, location)
                movements = Move_Out.objects.filter(
                    date__gte=init,
                    date__lte=end,
                    origin=location
                ).order_by('-date')
                context['date_report'] = movements

            del self.request.session['init_date']
            del self.request.session['end_date']
            del self.request.session['in_out']
            del self.request.session['location']

        return context


class LocationReportView(LoginRequiredMixin, FormView):
    form_class = LocationReportForm
    template_name = 'reporte/location/location_form.html'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('reporte:location')

    def form_valid(self, form):
        location = form.cleaned_data['location']
        in_out = form.cleaned_data['in_out']

        self.request.session['location'] = location
        self.request.session['in_out'] = in_out

        return super(LocationReportView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LocationReportView, self).get_context_data(**kwargs)
        context['locations'] = settings.LOCATIONS

        #if there is any info on session do:
        if 'location' in self.request.session and 'in_out' in self.request.session:
            status = self.request.session['in_out']
            location = self.request.session['location']
            #if status is IN:
            if status:
                if location == "Almacen":
                    movements = MoveIn.objects.filter(is_move_in=True).order_by('-date')
                    context['location_report'] = movements

                else:
                    movements = Move_Out.objects.filter(destiny=location).order_by('-date')
                    context['location_report'] = movements

            #if status is OUT:
            else:
                movements = Move_Out.objects.filter(origin=location).order_by('-date')
                context['location_report'] = movements

            context['status'] = status
            #Delete all session data
            del self.request.session['location']
            del self.request.session['in_out']

        return context


@login_required
def get_move_out_detail(request):
    pk = int(request.GET.get('move_out_pk', None))
    details = Move_Out.objects.get(pk=pk)
    authorized_by = User.objects.get(pk=details.authorized_by)
    received_by = User.objects.get(pk=details.received_by)
    given_by = User.objects.get(pk=details.given_by)
    data = {
        'product_class': str(details.product_class),
        'origin': details.origin,
        'destiny': details.destiny,
        'authorized_by': authorized_by.first_name + " " + authorized_by.last_name,
        'received_by': received_by.first_name + " " + received_by.last_name,
        'given_by': given_by.first_name + " " + given_by.last_name,
        'reason': details.reason,
        'reason_description': details.reason_description,
        'products': list(details.products.all().values_list('full_code')),
    }
    return HttpResponse(
        json.dumps(data),
        content_type='application/javascript; charset=utf8'
    )
