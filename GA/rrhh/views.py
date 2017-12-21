# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.views.generic import CreateView

from .models import Employee, Spouse, Spawn, Position, EmployeeControl, Control
from .forms import (
    EmployeeForm, SpouseForm, SpawnForm, 
    PositionForm, EmployeeControlForm, ControlForm
)

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


class EmployeeView(FormView):
    form_class = EmployeeForm
    template_name = 'rrhh/index.html'
    success_url = reverse_lazy('rrhh:employee')

    def get_context_data(self, **kwargs):
        context = super(EmployeeView, self).get_context_data(**kwargs)
        context['object_list'] = Employee.objects.all()
        return context


class SpouseView(FormView):
    form_class = SpouseForm
    model = Spouse
    template_name = 'rrhh/index.html'

class SpawnView(FormView):
    form_class = SpawnForm
    model = Spawn
    template_name = 'rrhh/index.html'

class PositionView(FormView):
    form_class = PositionForm
    model = Position
    template_name = 'rrhh/index.html'

class EmployeeControlView(FormView):
    form_class = EmployeeControlForm
    model = EmployeeControl
    template_name = 'rrhh/index.html'

class ControlView(FormView):
    form_class = ControlForm
    model = Control
    template_name = 'rrhh/index.html'