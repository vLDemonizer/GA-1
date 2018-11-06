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
    home_phone = models.CharField(max_length=40, blank=True, null=True)
    mobile_phone = models.CharField(max_length=40, blank=True, null=True)
    fecha_de_ingreso = models.DateField(blank=True, null=True, default='1994-11-24')
    salario = models.FloatField(blank=True, null=True, default=1)
    salario_comida = models.FloatField(blank=True, null=True, default=1)
    salario_transporte = models.FloatField(blank=True, null=True, default=1)
    bono = models.FloatField(blank=True, null=True, default=1)
    fao = models.BooleanField(default=False)
    ivss = models.BooleanField(default=False)

    def __str__(self):
        return str(
            self.name + ' ' + self.last_name
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

    