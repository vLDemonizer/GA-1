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
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.encoding import smart_bytes

from GA import settings


from .forms import (
    ProductClassForm, MoveInForm, MoveOutForm, UserCreateForm,
    LoginForm, CodesForm, PriceUpdateForm
)
from .models import ProductClass, Product, MoveIn, MoveOut, User, Move_Out
from .code_generator import generate_full_code, create_codes_file


class LandingPage(LoginRequiredMixin, TemplateView):
    template_name = 'inventario/home.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
        products = []
        for product in ProductClass.objects.all().order_by('name', 'product_type', 'size', 'brand'):
            if product.department == 'Equipos y Enseres' or product.department == 'Maquinaria' or product.department == 'Computacion':
                continue
            else:
                if product.low_stock:
                    setattr(product, 'stock_almacen', Product.objects.filter(product_class=product.pk, available=True, location=settings.PRIMARY_LOCATION).count())
                    products.append(product)

        context['products'] = products
        return context



class UserCreate(LoginRequiredMixin, FormView):
    form_class = UserCreateForm
    template_name = 'inventario/user/user_form.html'
    success_url = reverse_lazy('inventario:home')
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

        if "Save and Add another one" in form.cleaned_data['redirect']:
            self.success_url = reverse_lazy('inventario:move-in')

        return super(UserCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserCreate, self).get_context_data(**kwargs)
        context['is_superuser'] = json.dumps(self.request.user.is_superuser)
        return context


class ProductClassCreate(LoginRequiredMixin, CreateView):
    form_class = ProductClassForm
    template_name = 'inventario/product/product_class_form.html'
    success_url = reverse_lazy('inventario:home')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        if "Save and Add another one" in form.cleaned_data['redirect']:
            self.success_url = reverse_lazy('inventario:create-product')

        return super(ProductClassCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductClassCreate, self).get_context_data(**kwargs)
        context['is_superuser'] = json.dumps(self.request.user.is_superuser)
        context['is_staff'] = json.dumps(self.request.user.is_staff)
        return context


class ProductClassList(LoginRequiredMixin, FormView):
    form_class = ProductClassForm
    template_name = 'inventario/product/product_class_list.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('inventario:home')

    def form_valid(self, form):
        pk = form.cleaned_data['product_class']
        product_class = ProductClass.objects.get(pk=pk)
        product_class.name = form.cleaned_data['name']
        product_class.brand = form.cleaned_data['brand']
        product_class.product_type = form.cleaned_data['product_type']
        product_class.size = form.cleaned_data['size']
        product_class.department = form.cleaned_data['department']
        product_class.description = form.cleaned_data['description']
        product_class.min_amount = form.cleaned_data['min_amount']
        product_class.is_disposable = form.cleaned_data['is_disposable']
        product_class.cost_value = form.cleaned_data['cost_value']
        product_class.our_value = form.cleaned_data['our_value']
        product_class.their_value = form.cleaned_data['their_value']
        product_class.save()

        return super(ProductClassList, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductClassList, self).get_context_data(**kwargs)
        context['products'] = serializers.serialize(
            'json',
            ProductClass.objects.all().order_by('name')
        )
        return context


class MoveInCreate(LoginRequiredMixin, FormView):
    form_class = MoveInForm
    template_name = 'inventario/move/move_in_form.html'
    success_url = reverse_lazy('inventario:home')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        destiny = form.cleaned_data['destiny']
        pk = form.cleaned_data['product_class']
        amount = form.cleaned_data['amount']
        user = self.request.user
        products = []

        product_class = ProductClass.objects.get(pk=pk)
        move_in = MoveIn.objects.create(
            destiny=destiny,
            product_class=product_class,
        )
        amount_of_products = Product.objects.filter(
            product_class=product_class,
        ).count()

        for i in range(amount):
            product_number = amount_of_products + i + 1
            full_code = generate_full_code(
                user,
                product_class,
                product_number
            )
            product = Product.objects.create(
                product_class=product_class,
                full_code=full_code,
                available=True,
                location=destiny,
                number=product_number,
            )
            product.save()
            products.append(product)

        move_in.products.add(*products)

        if "Save and Add another one" in form.cleaned_data['redirect']:
            self.success_url = reverse_lazy('inventario:move-in')

        return super(MoveInCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(MoveInCreate, self).get_context_data(**kwargs)
        context['is_superuser'] = json.dumps(self.request.user.is_superuser)
        return context


class MoveOutView(LoginRequiredMixin, FormView):
    form_class = MoveOutForm
    template_name = 'inventario/move/move_out_form.html'
    success_url = reverse_lazy('inventario:home')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(MoveOutView, self).get_context_data(**kwargs)
        context['product_class'] = serializers.serialize(
            'json', ProductClass.objects.all())
        context['admin_users'] = serializers.serialize(
            'json', User.objects.filter(admin=True))
        context['retrieving_users'] = serializers.serialize(
            'json', User.objects.all())
        context['current_user'] = serializers.serialize(
            'json', [self.request.user])
        context['locations'] = json.dumps(settings.LOCATIONS)
        context['reasons'] = json.dumps(settings.MOVEMENT_REASONS)
        context['is_superuser'] = json.dumps(self.request.user.is_superuser)
        return context

    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        product_class_pk = form.cleaned_data['product_class']
        origin = settings.LOCATIONS[int(form.cleaned_data['from_location'])]
        destiny = settings.LOCATIONS[int(form.cleaned_data['destiny'])]
        reason = settings.MOVEMENT_REASONS[int(form.cleaned_data['reason'])]
        reason_description = form.cleaned_data['reason_description']
        authorized_by = form.cleaned_data['authorized_by']
        received_by = form.cleaned_data['received_by']
        given_by = self.request.user.pk

        product_class = ProductClass.objects.get(pk=product_class_pk)

        products = Product.objects.filter(
            product_class=product_class,
            location=origin,
        ).order_by('pk')[:amount]
        print(products)
        # If it's going to become unavailable
        if destiny == settings.LOCATIONS[4] or product_class.is_disposable:
            for product in products:
                product.location = destiny
                product.available = False
                product.save()
        else:
            for product in products:
                product.location = destiny
                product.save()

        move_out = Move_Out.objects.create(
            origin=origin,
            destiny=destiny,
            product_class=product_class,
            authorized_by=authorized_by,
            received_by=received_by,
            given_by=given_by,
            reason=reason,
            reason_description=reason_description,
        )
        move_out.products.add(*products)
        move_out.save()

        if "Save and Add another one" in form.cleaned_data['redirect']:
            self.success_url = reverse_lazy('inventario:move-out')
        return super(MoveOutView, self).form_valid(form)


class PrintCodes(LoginRequiredMixin, FormView):
    form_class = CodesForm
    template_name = 'inventario/product/print_product_codes.html'
    success_url = reverse_lazy('inventario:home')
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(PrintCodes, self).get_context_data(**kwargs)
        context['products'] = serializers.serialize(
            'json', ProductClass.objects.all()
        )
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        product_class = ProductClass.objects.get(pk=data['product_class'])
        products = Product.objects.filter(
            product_class=product_class,
            available=True,
            number__gte=data['start'],
            number__lte=data['end']
        ).order_by('number')
        create_codes_file(
            product_class,
            products,
            int(data['start']),
            int(data['end']),
            int(data['code_range'])
        )
        return super(PrintCodes, self).form_valid(form)


class PriceUpdateView(LoginRequiredMixin, FormView):
    form_class = PriceUpdateForm
    template_name = 'inventario/product/price_update_form.html'
    success_url = reverse_lazy('inventario:home')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        increment = float(form.cleaned_data['increment']) / 100
        print(increment)
        for product in ProductClass.objects.all():
            product.cost_value += product.cost_value * increment
            product.our_value += product.our_value * increment
            product.their_value += product.their_value * increment
            product.save()

        return super(PriceUpdateView, self).form_valid(form)



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
        content_type='application/javascript; charset=utf8'
    )


@login_required
def get_product_stock(request):
    pk = int(request.GET.get('product_class', None))
    location = int(request.GET.get('location', None))
    product_class = ProductClass.objects.get(pk=pk)
    stock = Product.objects.filter(
        product_class=product_class,
        location=settings.LOCATIONS[location],
        available=True,
    ).count()
    product = Product.objects.filter(
        product_class=product_class,
    ).order_by('-number')[0]
    code = product.full_code[:-15]
    series_limit = product.full_code[22:-9]
    unit_limit = product.full_code[28:]
    data = {
        'stock': stock,
        'code': code,
        'seriesLimit': series_limit,
        'unitLimit': unit_limit,
    }
    return HttpResponse(
        json.dumps(data),
        content_type='application/javascript; charset=utf8'
    )


@login_required
def get_product_global_stock(request):
    pk = int(request.GET.get('product_class', None))
    product_class = ProductClass.objects.get(pk=pk)
    stock = Product.objects.filter(
        product_class=product_class,
        available=True,
    ).count()
    return HttpResponse(
        json.dumps(stock),
        content_type='application/javascript; charset=utf8'
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
        content_type='application/javascript; charset=utf8'
    )


@login_required
def generate_file(request):
    data = request.GET
    pk = data.get('product_class', None)
    start = data.get('start', None)
    end = data.get('end', None)
    code_range = data.get('code_range', None)
    product_class = ProductClass.objects.get(pk=data['product_class'])
    name = "%s-codes.docx" % product_class
    products = Product.objects.filter(
        product_class=product_class,
        number__gte=data['start'],
        number__lte=data['end']
    ).order_by('number')
    document = create_codes_file(
        product_class,
        products,
        int(data['start']),
        int(data['end']),
        int(data['code_range'])
    )
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = "attachment; filename=%s" % name
    document.save(response)
    return response

@login_required
def make_single_move_out(request):
    data = request.GET
    product_class_pk = data['product_class']
    origin = settings.LOCATIONS[int(data['from_location'])]
    destiny = settings.LOCATIONS[int(data['destiny'])]
    reason = settings.MOVEMENT_REASONS[int(data['reason'])]
    reason_description = data.get('reason_description', None)
    authorized_by = data['authorized_by']
    received_by = data['received_by']
    series = data['series']
    unit = data['unit']
    given_by = request.user.pk
    data = True
    number = int(series + format(int(unit), '08d'))
    product_class = ProductClass.objects.get(pk=product_class_pk)
    try:
        product = Product.objects.get(
            product_class=product_class,
            available=True,
            location=origin,
            number=number,
        )

    except:
        data = False
        return HttpResponse(
            json.dumps(data),
            content_type='application/javascript; charset=utf8'
        )
    # If it's going to become unavailable
    if destiny == settings.LOCATIONS[4] or product_class.is_disposable:
        product.location = destiny
        product.available = False
        product.save()
    else:
        product.location = destiny
        product.save()

    move_out = Move_Out.objects.create(
        origin=origin,
        destiny=destiny,
        product_class=product_class,
        authorized_by=authorized_by,
        received_by=received_by,
        given_by=given_by,
        reason=reason,
        reason_description=reason_description,
    )
    move_out.products.add(product)
    move_out.save()
    return HttpResponse(
        json.dumps(data),
        content_type='application/javascript; charset=utf8'
    )
