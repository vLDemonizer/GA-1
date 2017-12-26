# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Employee, Spouse, Spawn, Position, EmployeeControl, ControlIn, ControlOut

admin.site.register(Employee)
admin.site.register(Spouse)
admin.site.register(Spawn)
admin.site.register(Position)
admin.site.register(EmployeeControl)
admin.site.register(ControlIn)
admin.site.register(ControlOut)
