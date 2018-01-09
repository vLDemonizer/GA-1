from django import forms
from django.forms import ModelForm

from .models import Employee, Spouse, Spawn, Position, EmployeeControl, ControlIn, ControlOut

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
            'cedula',
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
            'base_salary',
            'food_salary',
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

class ControlInForm(ModelForm):
    class Meta:
        model = ControlIn
        fields = [
            'product_class',
            'employee_control',
            'given',
            'taken_back'
        ]

class ControlOutForm(ModelForm):
    class Meta:
        model = ControlOut
        fields = [
            'control_in',
            'date',
            'taken',
        ]