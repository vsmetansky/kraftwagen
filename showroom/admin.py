from django.contrib import admin

from showroom.models import Employee, Position, Fullname

admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Fullname)
