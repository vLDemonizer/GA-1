from django import forms
from django.forms import widgets
from django.forms import ModelForm
from django.forms import modelformset_factory

from .models import Employee

class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeForm(ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'fecha_de_ingreso': DateInput(),
            'birthdate': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})

        self.fields['employee_id'].label = 'ID del Empleado (Capta Huella)'
        self.fields['name'].label = 'Nombre'     
        self.fields['last_name'].label = 'Apellido'
        self.fields['gender'].label = 'Genero'
        self.fields['birthdate'].label = 'Fecha de Nacimiento'
        self.fields['address'].label = 'Direccion'
        self.fields['civil_status'].label = 'Estado Civil'
        self.fields['home_phone'].label = 'Telefono Hogar'
        self.fields['mobile_phone'].label = 'Telefono Personal'

# class ProductForm(ModelForm):

#     class Meta:
#         model = Product
#         fields = '__all__'

# class EmployeeControlForm(ModelForm):

#     class Meta:
#         model = EmployeeControl
#         fields = ['product', 'date', 'amount']

# class EmployeeControlUpdateForm(ModelForm):

#     class Meta:
#         model = EmployeeControl
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(EmployeeControlUpdateForm, self).__init__(*args, **kwargs)
#         self.fields['employee'].widget.attrs.update({'class' : 'selectpicker show-tick', 'data-live-search': True})
#         self.fields['employee'].label = 'Empleado'
#         self.fields['type'].widget.attrs.update({'class' : 'selectpicker show-tick'})
#         self.fields['type'].label = 'Tipo'
#         self.fields['product'].widget.attrs.update({'class' : 'selectpicker show-tick', 'data-live-search': True})
#         self.fields['product'].label = 'Producto'
#         self.fields['date'].widget.attrs.update({'class' : 'form-control'})
#         self.fields['date'].label = 'Fecha'
#         self.fields['amount'].widget.attrs.update({'class' : 'form-control'})
#         self.fields['amount'].label = 'Cantidad'

# EmployeeControlFormset = modelformset_factory(
#     EmployeeControl,
#     can_delete=False,
#     extra=1,
#     form=EmployeeControlForm,
#     fields = ['product', 'date', 'amount']
# )