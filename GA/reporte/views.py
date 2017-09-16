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
from inventario.models import MoveIn, MoveOut, ProductClass, Product
from inventario.code_generator import *

class LandingPage(LoginRequiredMixin, TemplateView):
    template_name = 'reporte/home.html'
    login_url = reverse_lazy('inventario:login')

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
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

        product_class = ProductClass.objects.all().order_by('name')

        global_report = []
        wareHouse_value = 0;
        for product in product_class:
            stock_almacen = Product.objects.filter(product_class=product, available=True, location="Almacen").count()
            stock_oficina = Product.objects.filter(product_class=product, available=True, location="Oficina").count()
            stock_planta = Product.objects.filter(product_class=product, available=True, location="Planta").count()
            stock_mante = Product.objects.filter(product_class=product, available=True, location="Mantenimiento").count()
            stock_desin = Product.objects.filter(product_class=product, available=False).count()

            setattr(product, 'stock_almacen', stock_almacen)
            setattr(product, 'stock_oficina', stock_oficina)
            setattr(product, 'stock_planta', stock_planta)
            setattr(product, 'stock_mante', stock_mante)
            setattr(product, 'stock_desin', stock_desin)
            setattr(product, 'product_value', GeneralReportView.currency_format((product.their_value * product.stock)))

            global_report.append(product)

            wareHouse_value += product.their_value * product.stock

            print(product.currency_format())

        context['global_report'] = global_report
        context['wareHouse_value'] = GeneralReportView.currency_format(wareHouse_value)
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
            ProductClass.objects.all().order_by('name')
        )

        if 'product_class' in self.request.session:
            product_class = self.request.session['product_class']

            product = ProductClass.objects.get(pk=product_class)

            entrance = MoveIn.objects.filter(product_class=product_class).order_by('-date')
            movement = MoveOut.objects.filter(product_class=product_class).order_by('-date')

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
                if location == "Almacen":
                    movements = MoveIn.objects.filter(
                        date__gte=init,
                        date__lte=end
                    ).order_by('-date')
                    context['date_report'] = movements
                    print(movements[0].date)
                else:
                    movements = MoveOut.objects.filter(
                        date__gte=init,
                        date__lte=end,
                        origin=location
                    ).order_by('-date')
                    context['date_report'] = movements
            else:
                movements = MoveOut.objects.filter(
                    date__gte=init,
                    date__lte=end,
                    destiny=location,
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
                    movements = MoveIn.objects.all().order_by('-date')
                    context['location_report'] = movements

                else:
                    movements = MoveOut.objects.filter(destiny=location).order_by('-date')
                    context['location_report'] = movements

            #if status is OUT:
            else:
                movements = MoveOut.objects.filter(origin=location).order_by('-date')
                context['location_report'] = movements

            context['status'] = status
            #Delete all session data
            del self.request.session['location']
            del self.request.session['in_out']

        return context
