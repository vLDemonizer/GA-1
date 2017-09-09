from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from GA import settings

from GA import settings
from .forms import DateReportForm, ProductReportForm, LocationReportForm

# Create your views here.

class LandingPage(LoginRequiredMixin, TemplateView):
    template_name = 'reporte/home.html'
    login_url = reverse_lazy('inventario:login')

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
        return context

class DateReportView(LoginRequiredMixin, FormView):
    form_class = DateReportForm
    template_name = 'reporte/date/date_form.html'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('reporte:home')


class ProductReportView(LoginRequiredMixin, FormView):
    form_class = ProductReportForm
    template_name = 'reporte/product/product_form.html'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('reporte:home')

class LocationReportView(LoginRequiredMixin, FormView):
    form_class = LocationReportForm
    template_name = 'reporte/location/location_form.html'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('reporte:home')

    def form_valid(self, form):
        location = form.cleaned_data['location']
        choice = form.cleaned_data['choice']

        print(location, _in, _out)

        return super(LocationReportView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LocationReportView, self).get_context_data(**kwargs)
        context['locations'] = settings.LOCATIONS

        return context
