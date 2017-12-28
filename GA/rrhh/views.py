# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, TemplateView
from django.views.generic.edit import FormMixin, UpdateView
from django.views.generic.list import ListView

from .forms import (ControlInForm, ControlOutForm, EmployeeControlForm, EmployeeForm,
                    PositionForm, SpawnForm, SpouseForm)

from .models import ControlIn, ControlOut, Employee, EmployeeControl, Position, Spawn, Spouse
from inventario.models import ProductClass


class IndexRRHHView(LoginRequiredMixin, TemplateView):
    template_name = 'rrhh/index.html'
    login_url = reverse_lazy('inventario:login')


class EmployeeView(LoginRequiredMixin, CreateView):
    form_class = EmployeeForm
    template_name = 'rrhh/employee/employee-create.html'
    success_url = reverse_lazy('rrhh:index')
    login_url = reverse_lazy('inventario:login')

    def form_valid(self, form):
        return super(EmployeeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EmployeeView, self).get_context_data(**kwargs)
        context['object_list'] = Employee.objects.all()
        return context

class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = [
            'name',
            'last_name',
            'cedula',
            'gender',
            'birthdate',
            'address',
            'civil_status',
            'home_phone',
            'mobile_phone',
        ]
    template_name = 'rrhh/employee/employee-update.html'
    success_url = reverse_lazy('rrhh:index')

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdate, self).get_context_data(**kwargs)
        return context


class SpouseView(LoginRequiredMixin, CreateView):
    form_class = SpouseForm
    model = Spouse
    template_name = 'rrhh/employee/employee-spouse.html'
    success_url = reverse_lazy('rrhh:index')
    login_url = reverse_lazy('inventario:login')

    def form_valid(self, form):
        return super(SpouseView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SpouseView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.all()
        context['object_list'] = Spouse.objects.all()
        return context


class SpawnView(LoginRequiredMixin, CreateView):
    form_class = SpawnForm
    model = Spawn
    template_name = 'rrhh/employee/employee-spawn.html'
    success_url = reverse_lazy('rrhh:index')
    login_url = reverse_lazy('inventario:login')

    def form_valid(self, form):
        return super(SpawnView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SpawnView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.all()
        context['object_list'] = Spawn.objects.all()
        return context


class PositionView(LoginRequiredMixin, CreateView):
    form_class = PositionForm
    model = Position
    template_name = 'rrhh/employee/employee-position.html'
    success_url = reverse_lazy('rrhh:index')
    login_url = reverse_lazy('inventario:login')

    def form_valid(self, form):
        return super(PositionView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PositionView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.all()
        context['object_list'] = Position.objects.all()
        return context


class EmployeeControlView(LoginRequiredMixin, CreateView):
    form_class = EmployeeControlForm
    model = EmployeeControl
    template_name = 'rrhh/employee-control/employee-control.html'
    success_url = reverse_lazy('rrhh:index')
    login_url = reverse_lazy('inventario:login')

    def form_valid(self, form):
        return super(EmployeeControlView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EmployeeControlView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.all()
        context['object_list'] = EmployeeControl.objects.all()
        return context

class EmpoyeeControlUpdate(LoginRequiredMixin, UpdateView):
    model = EmployeeControl
    fields = [
            'employee',
            'date',
        ]
    
    template_name = 'rrhh/employee-control/employee-control-update.html'
    success_url = reverse_lazy('rrhh:index')

    def get_context_data(self, **kwargs):
        context = super(EmpoyeeControlUpdate, self).get_context_data(**kwargs)
        return context


class ControlInView(LoginRequiredMixin, CreateView):
    form_class = ControlInForm
    model = ControlIn
    template_name = 'rrhh/employee-control/employee-control-in.html'
    success_url = reverse_lazy('rrhh:index')
    login_url = reverse_lazy('inventario:login')

    def form_valid(self, form):
        return super(ControlInView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ControlInView, self).get_context_data(**kwargs)
        context['products']  = ProductClass.objects.all()
        context['employee_controls'] = EmployeeControl.objects.all()
        context['object_list'] = ControlIn.objects.all()
        return context


class ControlOutView(LoginRequiredMixin, CreateView):
    form_class = ControlOutForm
    model = ControlOut
    template_name = 'rrhh/employee-control/employee-control-out.html'
    success_url = reverse_lazy('rrhh:index')
    login_url = reverse_lazy('inventario:login')

    def form_valid(self, form):
        pk = form.cleaned_data['control_in']
        control_in = ControlIn.objects.get(pk=pk.pk)
        
        taken = form.cleaned_data['taken']

        if taken > control_in.given:
            form.add_error('taken', 'Cannot take back more than you gave in')
            return super(ControlOutView, self).form_invalid(form)
        if taken == control_in.given:
            control_in.taken_back = True
            control_in.save()
        
        return super(ControlOutView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ControlOutView, self).get_context_data(**kwargs)
        context['control_in'] = ControlIn.objects.filter(taken_back=False)
        context['object_list'] = ControlOut.objects.all()
        return context
