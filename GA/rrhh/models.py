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

    def __str__(self):
        return str(
            str(self.employee_id) + ' ' + self.name 
        )


class Spouse(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=128) # First and Second Name
    last_name = models.CharField(max_length=128) # First and Second Last Name
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='F')
    birthdate = models.DateField()
    mobile_phone = models.CharField(max_length=40)


class Spawn(models.Model):
    employee = models.ForeignKey(Employee, on_delete=None, blank=True, null=True)
    name = models.CharField(max_length=128) # First and Second Name
    last_name = models.CharField(max_length=128) # First and Second Last Name
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='F')
    birthdate = models.DateField()


class Position(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=128) # Position Full Name
    salary = models.FloatField()
    start = models.DateField() # Position Start Date
    end = models.DateField() # Position End Date
    is_active = models.BooleanField(default=True)
    pay_range = models.CharField(max_length=20, choices=PAY_RANGE_CHOICES, default='S')
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES, default='D')

    def __str__(self):
        return str(
            self.employee.name + ' ' + self.name
        )


class EmployeeControl(models.Model):
    """
    Control de productos de entrada por empleado por dia.
    """
    employee = models.ForeignKey(Employee, on_delete=None, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return str(
            self.employee.name + ' ' + self.date.strftime('%d-%m-%Y')
        )

class ControlIn(models.Model):
    """
    Control de Entrega de Productos al personal.
    """
    product_class = models.ForeignKey(ProductClass, on_delete=None, blank=True, null=True)
    employee_control = models.ForeignKey(EmployeeControl, on_delete=None, blank=True, null=True)
    given = models.IntegerField()
    taken_back = models.BooleanField()

    def __str__(self):
        return str(
            self.product_class.name + ' ' + str(self.given) + ' ' + self.employee_control.employee.name
        )
    

class ControlOut(models.Model):
    """
    Control de Retiro de Productos del Personal
    """
    control_in = models.ForeignKey(ControlIn, on_delete=None, blank=True, null=True)
    date = models.DateField()
    taken = models.IntegerField()