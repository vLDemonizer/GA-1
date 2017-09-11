from django import forms
from django.forms import ModelForm, TextInput, EmailInput, CheckboxInput, PasswordInput, DateInput

from GA import settings
from inventario.models import ProductClass, MoveIn, MoveOut, User

class GeneralReportForm(forms.Form):
    product_class = forms.IntegerField()

class DateReportForm(forms.Form):
    init_date = forms.CharField(widget=DateInput(attrs={'class': 'form-control'}), required=True)
    end_date = forms.CharField(widget=DateInput(attrs={'class': 'form-control'}), required=True)
    location = forms.CharField(max_length=30)
    in_out = forms.BooleanField(widget=CheckboxInput(attrs={'class': 'form-control'}), required=False)

class LocationReportForm(forms.Form):
    location = forms.CharField(max_length=30)
    in_out = forms.BooleanField(widget=CheckboxInput(attrs={'class': 'form-control'}), required=False)

class ProductReportForm(forms.Form):
    product_class = forms.IntegerField()
