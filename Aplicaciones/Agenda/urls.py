from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),

    # CRUD para Ciudades
    path('ciudades/', views.listar_ciudades, name='listar_ciudades'),
    path('ciudades/crear/', views.crear_ciudad, name='crear_ciudad'),
    path('ciudades/editar/<int:id_ciu>/', views.editar_ciudad, name='editar_ciudad'),
    path('ciudades/eliminar/<int:id_ciu>/', views.eliminar_ciudad, name='eliminar_ciudad'),

    # CRUD para Modelo
    path('modelos/', views.listar_modelos, name='listar_modelos'),
    path('modelos/crear/', views.crear_modelo, name='crear_modelo'),
    path('modelos/editar/<int:id_mod>/', views.editar_modelo, name='editar_modelo'),
    path('modelos/eliminar/<int:id_mod>/', views.eliminar_modelo, name='eliminar_modelo'),

    # CRUD para Propietario
    path('propietarios/', views.listar_propietarios, name='listar_propietarios'),
    path('propietarios/crear/', views.crear_propietario, name='crear_propietario'),
    path('propietarios/editar/<int:id_pro>/', views.editar_propietario, name='editar_propietario'),
    path('propietarios/eliminar/<int:id_pro>/', views.eliminar_propietario, name='eliminar_propietario'),

    # CRUD para Vehículo
    path('vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('vehiculos/crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/editar/<int:id_veh>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:id_veh>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
]