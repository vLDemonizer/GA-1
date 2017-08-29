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
