from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import ProductClass, Product, MoveIn, MoveOut, User


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
    model = ProductClass
    fields = [
        'name',
        'brand',
        'departament',
        'size',
        'description',
    ]
    template_name = 'inventario/product/product_class_form.html'


class MoveIn(CreateView):
    model = MoveIn
    fields = [
        'product_class'
    ]
    template_name = 'inventario/move/move_in_form.html'



def index(request):
    return render(request, 'index.html', {})
