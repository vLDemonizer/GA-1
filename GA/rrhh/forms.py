from django import forms
from django.forms import ModelForm

from .models import Employee, Spouse, Spawn, Position, EmployeeControl, Control

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

class SpouseForm(ModelForm):
    class Meta:
        model = Spouse
        fields = [
            'employee',
            'name',
            'last_name',
            'gender',
            'birthdate',
            'mobile_phone',
        ]

class SpawnForm(ModelForm):
    class Meta:
        model = Spawn
        fields = [
            'employee',    
            'name',    
            'last_name',   
            'gender',  
            'birthdate',   
        ]

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = [
            'employee',
            'name',
            'salary',
            'start',
            'end',
            'is_active',
            'pay_range',
            'shift',
        ]

class EmployeeControlForm(ModelForm):
    class Meta:
        model = EmployeeControl
        fields = [
            'employee',
            'date',
        ]

class ControlForm(ModelForm):
    class Meta:
        model = Control
        fields = [
            'product_class',
            'given',
            'received',
            'reason',
        ]