from django import forms
from django.forms import ModelForm, TextInput, EmailInput, CheckboxInput, PasswordInput
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
            'description',
        ]

class MoveInForm(ModelForm):
    amount = forms.IntegerField()

    class Meta:
        model = MoveIn
        fields = [
            'destiny',
            'product_class',
        ]

class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            'enterprise',
            'country',
            'city',
            'designation',
            'admin'
        ]
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
            'enterprise': TextInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'designation': TextInput(attrs={'class': 'form-control'}),
            'admin': CheckboxInput(attrs={'class': 'form-control'})
        }
