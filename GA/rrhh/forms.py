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

class EmployeeControlForm(ModelForm):

    class Meta:
        model = EmployeeControl
        fields = ['product', 'date', 'amount']

class EmployeeControlUpdateForm(ModelForm):

    class Meta:
        model = EmployeeControl
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeControlUpdateForm, self).__init__(*args, **kwargs)
        self.fields['employee'].widget.attrs.update({'class' : 'selectpicker show-tick', 'data-live-search': True})
        self.fields['type'].widget.attrs.update({'class' : 'selectpicker show-tick'})
        self.fields['product'].widget.attrs.update({'class' : 'selectpicker show-tick', 'data-live-search': True})
        self.fields['date'].widget.attrs.update({'class' : 'form-control'})
        self.fields['amount'].widget.attrs.update({'class' : 'form-control'})

EmployeeControlFormset = modelformset_factory(
    EmployeeControl,
    can_delete=False,
    extra=1,
    form=EmployeeControlForm,
    fields = ['product', 'date', 'amount']
)