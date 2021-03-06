from django import forms
from django.forms import ModelForm, TextInput, EmailInput, CheckboxInput, PasswordInput

from GA import settings
from .models import ProductClass, MoveIn, MoveOut, User

class ProductClassForm(ModelForm):
    redirect = forms.CharField(max_length=50, required=False)
    is_disposable = forms.BooleanField(widget=CheckboxInput, required=False)
    cost_value = forms.FloatField(required=False)
    our_value = forms.FloatField(required=False)
    their_value = forms.FloatField(required=False)
    product_class = forms.IntegerField(required=False)

    class Meta:
        model = ProductClass
        fields = [
            'name',
            'product_type',
            'brand',
            'department',
            'size',
            'min_amount',
            'description',
            'is_disposable',
            'cost_value',
            'our_value',
            'their_value',
        ]


class MoveInForm(forms.Form):
    amount = forms.IntegerField()
    redirect = forms.CharField(max_length=50, required=False)
    destiny = forms.CharField(max_length=30)
    product_class = forms.IntegerField()


class MoveOutForm(forms.Form):
    redirect = forms.CharField(max_length=50, required=False)
    amount = forms.IntegerField()
    authorized_by = forms.IntegerField()
    received_by = forms.IntegerField()
    given_by = forms.IntegerField()
    reason = forms.CharField(max_length=15)
    reason_description = forms.CharField(max_length=300, required=False)
    from_location = forms.CharField(max_length=30)
    destiny = forms.CharField(max_length=30)
    product_class = forms.IntegerField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserCreateForm(forms.Form):
    redirect = forms.CharField(max_length=50, required=False)
    first_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
    enterprise = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}), initial=settings.ENTERPRISE)
    country = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}), initial=settings.COUNTRY)
    city = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}), initial=settings.CITY)
    designation = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    admin = forms.BooleanField(widget=CheckboxInput(attrs={'class': 'form-control'}), required=False)


class CodesForm(forms.Form):
    product_class = forms.IntegerField()
    start = forms.IntegerField()
    end = forms.IntegerField()
    code_range = forms.IntegerField()


class PriceUpdateForm(forms.Form):
    increment = forms.FloatField()