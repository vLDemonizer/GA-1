# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, TemplateView, DeleteView, DetailView
from django.views.generic.edit import FormMixin, UpdateView
from django.views.generic.list import ListView

from .forms import (EmployeeControlForm, EmployeeForm, ProductForm, EmployeeControlFormset, EmployeeControlUpdateForm)

from .models import Employee, EmployeeControl, Product
from inventario.models import ProductClass


class IndexRRHHView(LoginRequiredMixin, TemplateView):
    template_name = 'rrhh/index.html'
    login_url = reverse_lazy('inventario:login')


class ListEmployee(LoginRequiredMixin, TemplateView):
    template_name = 'rrhh/employee/employee-list.html'
    login_url = reverse_lazy('inventario:login')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
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
    template_name = 'rrhh/employee/employee-detail.html'
    context_object_name = 'employee'
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


# Control Views
class EmployeeControlView(LoginRequiredMixin, CreateView):
    form_class = EmployeeControlForm
    template_name = 'rrhh/employee-control/control_form.html'
    model = EmployeeControl
    pk_url_kwarg = 'pk'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('rrhh:employee-list')

    def get_queryset(self):
        employee_pk = self.kwargs.get(self.pk_url_kwarg)
        return Employee.objects.get(pk=employee_pk)

    def form_valid(self, form):
        if form.is_valid():
            control = form.save(commit=False)
            control.type = 'I'
            control.employee = self.get_queryset()
            control.save()

            return super().form_valid(form)

        return super().form_invalid(form)
            

    def get_context_data(self, **kwargs):
        context = super(EmployeeControlView, self).get_context_data(**kwargs)
        context['employee'] = self.get_queryset()
        context['products'] = ProductClass.objects.all()
        context['agregar'] = True
        return context


class EmployeeControlDeleteView(LoginRequiredMixin, CreateView):
    form_class = EmployeeControlForm
    template_name = 'rrhh/employee-control/control_form.html'
    model = EmployeeControl
    pk_url_kwarg = 'pk'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('rrhh:employee-list')

    def get_queryset(self):
        employee_pk = self.kwargs.get(self.pk_url_kwarg)
        return Employee.objects.get(pk=employee_pk)

    def form_valid(self, form):
        if form.is_valid():
            control = form.save(commit=False)
            control.type = 'O'
            control.employee = self.get_queryset()
            control.save()

            return super().form_valid(form)

        return super().form_invalid(form)
            

    def get_context_data(self, **kwargs):
        context = super(EmployeeControlDeleteView, self).get_context_data(**kwargs)
        context['employee'] = self.get_queryset()
        context['products'] = ProductClass.objects.all()
        context['agregar'] = False
        return context


class EmployeeControlListView(LoginRequiredMixin, ListView):
    template_name = 'rrhh/employee-control/control-list.html'
    model = EmployeeControl
    context_object_name = 'controls'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('rrhh:index')

class EmployeeControlUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'rrhh/product/product_form.html'
    model = EmployeeControl
    form_class = EmployeeControlUpdateForm
    pk_url_kwarg = 'pk'
    login_url = reverse_lazy('inventario:login')

    def get_success_url(self):
        return reverse('rrhh:employee-detail', kwargs={'pk': self.kwargs.get('employee')})


class EmployeeControlRemoveView(LoginRequiredMixin, DeleteView):
    template_name = 'rrhh/employee-control/control-remove.html'
    model = EmployeeControl
    pk_url_kwarg = 'pk'
    login_url = reverse_lazy('inventario:login')
    success_url = reverse_lazy('rrhh:employee-control-list')