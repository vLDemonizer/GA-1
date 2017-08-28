from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ProductClassForm
from .models import ProductClass, Product, MoveIn, MoveOut, User


class LandingPage(TemplateView):
    template_name = 'inventario/home.html'

class UserCreate(CreateView):
    model = User
    fields = [
        'username',
        'password',
        'first_name',
        'last_name',
        'designation',
    ]
    template_name = 'inventario/user/user_form.html'


class ProductClassCreate(CreateView):
    form_class = ProductClassForm
    template_name = 'inventario/product/product_class_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if "Save and Add another one" in form.cleaned_data['redirect']:
            self.success_url = reverse_lazy('create-product')

        return super(ProductClassCreate, self).form_valid(form)

class MoveIn(CreateView):
    model = MoveIn
    fields = [
        'product_class'
    ]
    template_name = 'inventario/move/move_in_form.html'
