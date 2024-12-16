from django.contrib import admin
from .models import Ciudad, Modelo, Propietario, Vehiculo

# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Modelo)
admin.site.register(Propietario)
admin.site.register(Vehiculo)

