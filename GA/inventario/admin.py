from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, ProductClass, Product, MoveIn, MoveOut, User, Move_Out

admin.site.register(User)
admin.site.register(ProductClass)
admin.site.register(Product)
admin.site.register(MoveIn)
admin.site.register(MoveOut)
admin.site.register(Move_Out)
