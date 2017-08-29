from django import forms
from django.forms import ModelForm, TextInput, EmailInput, CheckboxInput, PasswordInput

from GA import settings
from .models import ProductClass, MoveIn, User

class ProductClassForm(ModelForm):
    redirect = forms.CharField(max_length=50, required=False)

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
        ]


class MoveInForm(forms.Form):
    amount = forms.IntegerField()
    redirect = forms.CharField(max_length=50, required=False)
    destiny = forms.CharField(max_length=30)
    product_class = forms.IntegerField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserCreateForm(forms.Form):
    first_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
    enterprise = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}), initial=settings.ENTERPRISE)
    country = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}), initial=settings.COUNTRY)
    city = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}), initial=settings.CITY)
    designation = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    admin = forms.BooleanField(widget=CheckboxInput(attrs={'class': 'form-control'}))
