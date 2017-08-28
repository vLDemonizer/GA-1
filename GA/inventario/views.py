import json

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ProductClassForm, MoveInForm, UserCreateForm
from .models import ProductClass, Product, MoveIn, MoveOut, User


class LandingPage(TemplateView):
    template_name = 'inventario/home.html'


class UserCreate(CreateView):
    form_class = UserCreateForm
    template_name = 'inventario/user/user_form.html'
    success_url = ''


class ProductClassCreate(CreateView):
    form_class = ProductClassForm
    template_name = 'inventario/product/product_class_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if "Save and Add another one" in form.cleaned_data['redirect']:
            self.success_url = reverse_lazy('create-product')

        return super(ProductClassCreate, self).form_valid(form)

class MoveIn(CreateView):
    form_class = MoveInForm
    template_name = 'inventario/move/move_in_form.html'


def get_product_class_details(request):
    pk = request.GET.get('product_class', None)
    details = ProductClass.objects.get(pk=pk)
    data = {
        'name': details.name,
        'product_type': details.product_type,
        'brand': details.brand,
        'department': details.department,
        'size': details.size,
    }
    return HttpResponse(
        json.dumps(data),
        content_type = 'application/javascript; charset=utf8'
    )

def get_products(request):
    status = request.GET.get('products', None)
    if status:
        products = ProductClass.objects.all()
        p = []
        for product in products:
            p.append({
                'pk': product.pk,
                'name': product.name,
                'type': product.product_type,
                'brand': product.brand,
                'department': product.department,
                'size': product.size,
                'code': product.code,
            })
        data = {
            'products': p
        }

    return HttpResponse(
        json.dumps(data),
        content_type = 'application/javascript; charset=utf8'
    )
