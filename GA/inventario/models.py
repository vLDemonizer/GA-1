from random import randint
from django.utils import timezone

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
    is_disposable = models.BooleanField(default=False)
    cost_value = models.FloatField(default=0)
    our_value = models.FloatField(default=0)
    their_value = models.FloatField(default=0)

    def __str__(self):
        return (
            self.name + ' ' + self.product_type + ' '
            + self.size +  ' ' + self.brand + ' '
            + self.department
        )

    @property
    def product_limit(self):
        return self.product_set.count()

    @property
    def low_stock(self):
        if self.product_set.filter(available=True, location=settings.PRIMARY_LOCATION).count() <= self.min_amount:
            return True
        return False

    @property
    def stock(self):
        return self.product_set.filter(available=True).count()

    def currency_format(self):
        return "{:,.2f} Bs".format(self.their_value)

    def clean_fields(self, exclude=None):
        super(ProductClass, self).clean_fields(exclude=exclude)
        try:
            ProductClass.objects.get(
                name=self.name,
                product_type=self.product_type,
                brand=self.brand,
                department=self.department,
                size=self.size,
                min_amount=self.min_amount,
                is_disposable=self.is_disposable,
                cost_value=self.cost_value,
                our_value=self.our_value,
                their_value=self.their_value,
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
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.product_class.name + '-' + self.full_code


class MoveIn(models.Model):
    destiny = models.CharField(max_length=30, default=settings.PRIMARY_LOCATION)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date = models.DateTimeField()
    is_move_in = models.BooleanField(default=True)

    def __str__(self):
        return self.product_class.name + ' Moved in on the ' + str(self.date)

    def save(self, *args, **kwargs):
        "On creation, add timestamp"
        if not self.id:
            self.date = timezone.now()
        return super(MoveIn, self).save(*args, **kwargs)


class MoveOut(MoveIn):
    origin = models.CharField(max_length=30, default=settings.PRIMARY_LOCATION)
    authorized_by = models.SmallIntegerField(blank=False)
    received_by = models.SmallIntegerField(blank=False)
    given_by = models.SmallIntegerField(blank=False)
    reason = models.CharField(max_length=15)
    reason_description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return (
            self.product_class.name + ' %d' % self.products.count()
            + ' Moved out on the ' + str(self.date)
            + ' ' + self.reason + ' From: ' + self.origin
            + ' To: ' + self.destiny
        )


class Move_Out(models.Model):
    destiny = models.CharField(max_length=30, default=settings.PRIMARY_LOCATION)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date = models.DateTimeField()
    origin = models.CharField(max_length=30, default=settings.PRIMARY_LOCATION)
    authorized_by = models.SmallIntegerField(blank=False)
    received_by = models.SmallIntegerField(blank=False)
    given_by = models.SmallIntegerField(blank=False)
    reason = models.CharField(max_length=15)
    reason_description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return (
            self.product_class.name + ' %d' % self.products.count()
            + ' Moved out on the ' + str(self.date)
            + ' ' + self.reason + ' From: ' + self.origin
            + ' To: ' + self.destiny
        )

    def save(self, *args, **kwargs):
        "On creation, add timestamp"
        if not self.date:
            self.date = timezone.now()
        return super(Move_Out, self).save(*args, **kwargs)


class User(AbstractUser):
    enterprise = models.CharField(max_length=20, default=settings.ENTERPRISE)
    country = models.CharField(max_length=20, default=settings.COUNTRY)
    city = models.CharField(max_length=50, default=settings.CITY)
    designation =  models.CharField(max_length=50)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.designation + ' - ' + self.first_name + ' ' + self.last_name
