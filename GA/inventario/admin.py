from django.contrib import admin

from .models import ProductClass, Product, MoveIn, MoveOut, User

admin.site.register(ProductClass)
admin.site.register(Product)
admin.site.register(MoveIn)
admin.site.register(MoveOut)
admin.site.register(User)
# Register your models here.
