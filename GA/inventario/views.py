import json

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ProductClassForm, MoveInForm, MoveOutForm, UserCreateForm, LoginForm
from .models import ProductClass, Product, MoveIn, MoveOut, User


class LandingPage(LoginRequiredMixin, TemplateView):
    template_name = 'inventario/home.html'
    login_url = reverse_lazy('login')


class Login(FormView):
    form_class = LoginForm
    template_name = 'inventario/user/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super(Login, self).form_valid(form)
        else:
            form.add_error('username','No user found')
            return super(Login, self).form_invalid(form)


class UserCreate(LoginRequiredMixin, FormView):
    form_class = UserCreateForm
    template_name = 'inventario/user/user_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        enterprise = form.cleaned_data['enterprise']
        country = form.cleaned_data['country']
        city = form.cleaned_data['city']
        designation = form.cleaned_data['designation']
        admin = form.cleaned_data['admin']
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
        except:
            form.add_error('username', 'User already exist')
            return super(UserCreate, self).form_invalid(form)
        user.enterprise = enterprise
        user.country = country
        user.city = city
        user.designation = designation
        user.admin = admin
        user.save()

        return super(UserCreate, self).form_valid(form)


class ProductClassCreate(LoginRequiredMixin, CreateView):
    form_class = ProductClassForm
    template_name = 'inventario/product/product_class_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        if "Save and Add another one" in form.cleaned_data['redirect']:
            self.success_url = reverse_lazy('create-product')

        return super(ProductClassCreate, self).form_valid(form)

class MoveIn(LoginRequiredMixin, FormView):
    form_class = MoveInForm
    template_name = 'inventario/move/move_in_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        if "Save and Add another one" in form.cleaned_data['redirect']:
            self.success_url = reverse_lazy('move-in')

        destiny = form.cleaned_data['destiny']
        pk = form.cleaned_data['product_class']
        print(pk)
        product_class = ProductClass.objects.get(pk=pk)
        amount = form.cleaned_data['amount']
        product = Product.objects.create(
            product_class=product_class,
            full_code='Dummy' + str(amount),
            available=True,
            location=destiny
        )
        print(product_class.pk)
        print(product)
        print(form.cleaned_data['destiny'])
        print(form.cleaned_data['product_class'])
        print(form.cleaned_data['amount'])


        return super(MoveIn, self).form_valid(form)

class MoveOut(LoginRequiredMixin, FormView):
    form_class = MoveInForm
    template_name = 'inventario/move/move_out_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

@login_required
def log_out(request):
    logout(request)
    print('login out')
    return redirect(reverse_lazy('login'))


@login_required
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


@login_required
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
