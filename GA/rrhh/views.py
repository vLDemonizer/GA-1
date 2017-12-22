# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView

from .forms import (ControlInForm, ControlOutForm, EmployeeControlForm, EmployeeForm,
                    PositionForm, SpawnForm, SpouseForm)
from .models import ControlIn, ControlOut, Employee, EmployeeControl, Position, Spawn, Spouse


"""
class FormListView(FormView, ListView):
    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        #From BaseListView
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})

        context = self.get_context_data(object_list=self.object_list, form=self.form, kwargs=**kwargs)
        return self.render_to_response(context)
        
    def get_context_data(self, object_list, form, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        context['object_list'] = object_list
        context['form'] = form
        return context
"""


class IndexRRHHView(TemplateView):
    template_name = 'rrhh/index.html'


class EmployeeView(CreateView):
    form_class = EmployeeForm
    template_name = 'rrhh/index.html'
    success_url = reverse_lazy('rrhh:employee')

    def form_valid(self, form):
        return super(EmployeeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EmployeeView, self).get_context_data(**kwargs)
        context['object_list'] = Employee.objects.all()
        return context


class SpouseView(CreateView):
    form_class = SpouseForm
    model = Spouse
    template_name = 'rrhh/index.html'
    success_url = reverse_lazy('rrhh:spouse')

    def form_valid(self, form):
        return super(SpouseView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SpouseView, self).get_context_data(**kwargs)
        context['object_list'] = Spouse.objects.all()
        return context

class SpawnView(CreateView):
    form_class = SpawnForm
    model = Spawn
    template_name = 'rrhh/index.html'
    success_url = reverse_lazy('rrhh:spawn')

    def form_valid(self, form):
        return super(SpawnView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SpawnView, self).get_context_data(**kwargs)
        context['object_list'] = Spawn.objects.all()
        return context

class PositionView(CreateView):
    form_class = PositionForm
    model = Position
    template_name = 'rrhh/index.html'
    success_url = reverse_lazy('rrhh:position')

    def form_valid(self, form):
        return super(PositionView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PositionView, self).get_context_data(**kwargs)
        context['object_list'] = Position.objects.all()
        return context

class EmployeeControlView(CreateView):
    form_class = EmployeeControlForm
    model = EmployeeControl
    template_name = 'rrhh/index.html'
    success_url = reverse_lazy('rrhh:employee-control')

    def form_valid(self, form):
        return super(EmployeeControlView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EmployeeControlView, self).get_context_data(**kwargs)
        context['object_list'] = EmployeeControl.objects.all()
        return context

class ControlInView(CreateView):
    form_class = ControlInForm
    model = ControlIn
    template_name = 'rrhh/index.html'
    success_url = reverse_lazy('rrhh:control-in')

    def form_valid(self, form):
        return super(ControlInView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ControlInView, self).get_context_data(**kwargs)
        context['object_list'] = ControlIn.objects.all()
        return context

class ControlOutView(CreateView):
    form_class = ControlOutForm
    model = ControlOut
    template_name = 'rrhh/index.html'
    success_url = reverse_lazy('rrhh:control-out')

    def form_valid(self, form):
        pk = form.cleaned_data['control_in']
        control_in = ControlIn.objects.get(pk=pk.pk)
        
        taken = form.cleaned_data['taken']

        if taken > control_in.given:
            form.add_error('taken', 'Cannot take back more than you give in')
            return super(ControlOutView, self).form_invalid(form)
        
        return super(ControlOutView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ControlOutView, self).get_context_data(**kwargs)
        context['object_list'] = ControlOut.objects.all()
        return context
