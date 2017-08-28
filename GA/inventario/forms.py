from django import forms
from django.forms import ModelForm
from .models import ProductClass

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
