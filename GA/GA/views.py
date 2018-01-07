import json
import os

from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView, ListView

from django.urls import reverse_lazy


from GA import settings


from inventario.forms import  LoginForm

from inventario.models import User
from inventario.code_generator import generate_full_code, create_codes_file

class Login(FormView):
    form_class = LoginForm
    template_name = 'inventario/user/login.html'
    success_url = reverse_lazy('home')
    redirect_field_name = 'redirect_to'
    redirect_authenticated_user = True

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('inventario:home'))

        return super(Login, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super(Login, self).form_valid(form)
        else:
            form.add_error('username', 'No user found')
            return super(Login, self).form_invalid(form)

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = reverse_lazy('login')


@login_required
def log_out(request):
    logout(request)
    return redirect(reverse_lazy('login'))