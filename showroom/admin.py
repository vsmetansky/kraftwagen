from django.contrib import admin

from showroom.models import Employee, Position, Fullname, Facility, BodyType, Car, Client, Manufacturer

admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Fullname)

admin.site.register(Manufacturer)
admin.site.register(Facility)
admin.site.register(BodyType)
admin.site.register(Car)

admin.site.register(Client)
