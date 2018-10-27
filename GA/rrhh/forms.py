from django import forms
from django.forms import ModelForm
from django.forms import modelformset_factory

from .models import Employee, EmployeeControl, Product

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = [
            'employee_id',
            'name',
            'last_name',
            'cedula',
            'gender',
            'birthdate',
            'address',
            'civil_status',
            'home_phone',
            'mobile_phone',
        ]

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class EmployeeControlFrom(ModelForm):

    class Meta:
        model = EmployeeControl
        fields = '__all__'

EmployeeControlFormset = modelformset_factory(
    EmployeeControl,
    can_delete=False,
    extra=1,
    form=EmployeeControlFrom,
    fields = ['employee', 'product', 'type', 'date']
)