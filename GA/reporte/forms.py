from django import forms
from django.forms import ModelForm, TextInput, EmailInput, CheckboxInput, PasswordInput, DateInput

from GA import settings
from inventario.models import ProductClass, MoveIn, MoveOut, User

class GeneralReportForm(forms.Form):
    product_class = forms.IntegerField()

class DateReportForm(forms.Form):
    product_class = forms.IntegerField()

class LocationReportForm(forms.Form):
    product_class = forms.IntegerField()

class ProductReportForm(forms.Form):
    product_class = forms.IntegerField()
