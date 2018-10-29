# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from inventario.models import ProductClass


GENDER_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otros'),
)

CIVIL_CHOICES = (
    ('S', 'Soltero'),
    ('C', 'Casado'),
    ('V', 'Viudo'),
)

PAY_RANGE_CHOICES = (
    ('S', 'Semanal'),
    ('Q', 'Quincenal'),
)

SHIFT_CHOICES = (
    ('D', 'Diurno'),
    ('N', 'Nocturno'),
    ('M', 'Mixto'),
)


class Employee(models.Model):
    employee_id = models.IntegerField(unique=True)  # Fingerprint ID
    name = models.CharField(max_length=128) # First and Second Name
    last_name = models.CharField(max_length=128) # First and Second Last Name
    cedula = models.IntegerField(unique=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='M')
    birthdate = models.DateField()
    address = models.CharField(max_length=256)
    civil_status = models.CharField(max_length=20, choices=CIVIL_CHOICES, default='S')
    home_phone = models.CharField(max_length=40)
    mobile_phone = models.CharField(max_length=40)
    fecha_de_ingreso = models.DateField(blank=True, null=True)
    salario = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(
            self.name + ' ' + self.last_name
        )


class Spouse(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=128) # First and Second Name
    last_name = models.CharField(max_length=128) # First and Second Last Name
    cedula = models.IntegerField(unique=True, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='F')
    birthdate = models.DateField()
    mobile_phone = models.CharField(max_length=40)

    def __str__(self):
        return str(
            str(self.employee.employee_id) + ' ' + self.name + ' ' + self.last_name
        )


class Spawn(models.Model):
    """
    Childs of the employee
    """
    employee = models.ForeignKey(Employee, on_delete=None, blank=True, null=True)
    name = models.CharField(max_length=128) # First and Second Name
    last_name = models.CharField(max_length=128) # First and Second Last Name
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='F')
    birthdate = models.DateField()

    def __str__(self):
        return str(
            str(self.employee.employee_id) + ' ' + self.name + ' ' + self.last_name
        )


class Position(models.Model):
    """
    Description of the shift, salary and position in the enterprise
    """
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=128) # Position Full Name
    base_salary = models.FloatField(default=0)
    food_salary = models.FloatField(default=0)
    start = models.DateField() # Position Start Date
    end = models.DateField() # Position End Date
    is_active = models.BooleanField(default=True)
    pay_range = models.CharField(max_length=20, choices=PAY_RANGE_CHOICES, default='S')
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES, default='D')

    def __str__(self):
        return str(
            str(self.employee.employee_id) + ' ' + self.employee.name + ' ' + self.name + ' ' + str(self.salary)
        )


class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    type = models.CharField(max_length=250, help_text="Talla, Color o Descripcion", default='')
    
class EmployeeControl(models.Model):
    CONTROL_TYPE = (
        ('I', 'Agregar'),
        ('O', 'Quitar'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(ProductClass, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=20, choices=CONTROL_TYPE, default='I')
    date = models.DateField()
    amount = models.IntegerField(default=1)

    