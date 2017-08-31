from random import randint

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

from GA import settings


def generate_product_code():
    while True:
        code = str(hex(randint(100000, 1000000))[2:]).upper()
        if not ProductClass.objects.filter(code=code).exists():
            return code


class ProductClass(models.Model):
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    brand = models.CharField(max_length=30)
    department = models.CharField(max_length=50)
    size = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(max_length=120, blank=True)
    code = models.CharField(max_length=5, unique=True, default=generate_product_code)
    min_amount = models.SmallIntegerField(blank=True, null=True)
    is_liquid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def clean_fields(self, exclude=None):
        super(ProductClass, self).clean_fields(exclude=exclude)
        try:
            ProductClass.objects.get(
                name=self.name,
                product_type=self.product_type,
                brand=self.brand,
                department=self.department,
                size=self.size,
            )
        except:
            return
        raise ValidationError({
            'name': _('There is already another product in the database with this same characteristics')
        })


class Product(models.Model):
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE)
    full_code = models.CharField(max_length=60, blank=True, unique=True)
    available = models.BooleanField(default=True)
    location = models.CharField(max_length=30, default=settings.PRIMARY_LOCATION)

    def __str__(self):
        return self.product_class.name + '-' + self.full_code


class MoveIn(models.Model):
    destiny = models.CharField(max_length=30, default=settings.PRIMARY_LOCATION)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_class.name + ' Moved in on the ' + str(self.date)


class MoveOut(MoveIn):
    authorized_by = models.SmallIntegerField(blank=False)
    received_by = models.SmallIntegerField(blank=False)
    given_by = models.SmallIntegerField(blank=False)
    reason = models.CharField(max_length=15)
    reason_description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.product_class.name + ' Moved out on the ' + str(self.date) + ' ' + self.reason


class User(AbstractUser):
    enterprise = models.CharField(max_length=20, default=settings.ENTERPRISE)
    country = models.CharField(max_length=20, default=settings.COUNTRY)
    city = models.CharField(max_length=50, default=settings.CITY)
    designation =  models.CharField(max_length=50)
    admin = models.BooleanField(default=False)
    move_out = models.ForeignKey(MoveOut, blank=True, null=True)

    def __str__(self):
        return self.designation + ' - ' + self.first_name + ' ' + self.last_name
