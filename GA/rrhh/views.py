# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, TemplateView, DeleteView, DetailView, TemplateView
from django.views.generic.edit import FormMixin, UpdateView
from django.views.generic.list import ListView

from .forms import (EmployeeControlFrom, EmployeeForm, ProductForm, EmployeeControlFormset)

from .models import Employee, EmployeeControl, Product
from inventario.models import ProductClass


class IndexRRHHView(LoginRequiredMixin, TemplateView):
    template_name = 'rrhh/index.html'
    login_url = reverse_lazy('inventario:login')


class ListEmployee(LoginRequiredMixin, TemplateView):
    template_name = 'rrhh/employee/employee-list.html'
    login_url = reverse_lazy('inventario:login')
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        formset = context['control_formset']

        if formset.is_valid():
            for form in formset:
                form.save()
        else:
            print("bad form")
        return self.render_to_response(context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()

        if self.request.POST:
            context['control_formset'] = EmployeeControlFormset(self.request.POST)
        else:
            context['control_formset'] = EmployeeControlFormset(queryset=EmployeeControl.objects.none())
        return context

class CreateEmployee(LoginRequiredMixin, CreateView):
    template_name = 'rrhh/employee/employee-create.html'
    model = Employee
    form_class = EmployeeForm
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('rrhh:index')

class UpdateEmployee(LoginRequiredMixin, UpdateView):
    template_name = 'rrhh/employee/employee-create.html'
    model = Employee
    form_class = EmployeeForm
    pk_url_kwarg = 'pk'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('rrhh:employee-list')

class DeleteEmployee(LoginRequiredMixin, DeleteView):
    template_name = 'rrhh/employee/employee-delete.html'
    model = Employee
    pk_url_kwarg = 'pk'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('rrhh:employee-list')

class DetailEmployee(LoginRequiredMixin, DetailView):
    template_name = 'rrhh/employee/employee-delete.html'
    model = Employee
    pk_url_kwarg = 'pk'
    login_url = reverse_lazy('inventario:login')


# Products Views
class CreateProduct(LoginRequiredMixin, CreateView):
    template_name = 'rrhh/product/product_form.html'
    model = Product
    form_class = ProductForm
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('rrhh:index')

class UpdateProduct(LoginRequiredMixin, UpdateView):
    template_name = 'rrhh/product/product_form.html'
    model = Product
    form_class = ProductForm
    pk_url_kwarg = 'pk'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('rrhh:product-list')

class ListProduct(LoginRequiredMixin, ListView):
    template_name = 'rrhh/product/product_list.html'
    model = Product
    context_object_name = 'products'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('rrhh:index')


