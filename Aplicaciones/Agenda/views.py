from django.shortcuts import render, get_object_or_404, redirect
from .models import Ciudad, Modelo, Propietario, Vehiculo

# Create your views here.

def home(request):
    return render(request,"home.html")

# CRUD para Ciudad
def listar_ciudades(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'listar_ciudades.html', {'ciudades': ciudades})

def crear_ciudad(request):
    if request.method == 'POST':
        nombre_ciu = request.POST['nombre_ciu']
        Ciudad.objects.create(nombre_ciu=nombre_ciu)
        return redirect('listar_ciudades')
    return render(request, 'crear_ciudad.html')

def editar_ciudad(request, id_ciu):
    ciudad = get_object_or_404(Ciudad, id_ciu=id_ciu)
    if request.method == 'POST':
        ciudad.nombre_ciu = request.POST['nombre_ciu']
        ciudad.save()
        return redirect('listar_ciudades')
    return render(request, 'editar_ciudad.html', {'ciudad': ciudad})

def eliminar_ciudad(request, id_ciu):
    ciudad = get_object_or_404(Ciudad, id_ciu=id_ciu)
    ciudad.delete()
    return redirect('listar_ciudades')

# CRUD para Modelo
def listar_modelos(request):
    modelos = Modelo.objects.all()
    return render(request, 'listar_modelos.html', {'modelos': modelos})

def crear_modelo(request):
    if request.method == 'POST':
        nombre_mod = request.POST['nombre_mod']
        Modelo.objects.create(nombre_mod=nombre_mod)
        return redirect('listar_modelos')
    return render(request, 'crear_modelo.html')

def editar_modelo(request, id_mod):
    modelo = get_object_or_404(Modelo, id_mod=id_mod)
    if request.method == 'POST':
        modelo.nombre_mod = request.POST['nombre_mod']
        modelo.save()
        return redirect('listar_modelos')
    return render(request, 'editar_modelo.html', {'modelo': modelo})

def eliminar_modelo(request, id_mod):
    modelo = get_object_or_404(Modelo, id_mod=id_mod)
    modelo.delete()
    return redirect('listar_modelos')

# CRUD para Propietario
def listar_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'listar_propietarios.html', {'propietarios': propietarios})

def crear_propietario(request):
    if request.method == 'POST':
        nombre_pro = request.POST['nombre_pro']
        apellido_pro = request.POST['apellido_pro']
        email_pro = request.POST['email_pro']
        telefono_pro = request.POST['telefono_pro']
        fk_id_ciu = get_object_or_404(Ciudad, id_ciu=request.POST['fk_id_ciu'])
        Propietario.objects.create(
            nombre_pro=nombre_pro, apellido_pro=apellido_pro,
            email_pro=email_pro, telefono_pro=telefono_pro, fk_id_ciu=fk_id_ciu
        )
        return redirect('listar_propietarios')
    return render(request, 'crear_propietario.html', {'ciudades': Ciudad.objects.all()})

def editar_propietario(request, id_pro):
    propietario = get_object_or_404(Propietario, id_pro=id_pro)
    if request.method == 'POST':
        propietario.nombre_pro = request.POST['nombre_pro']
        propietario.apellido_pro = request.POST['apellido_pro']
        propietario.email_pro = request.POST['email_pro']
        propietario.telefono_pro = request.POST['telefono_pro']
        propietario.fk_id_ciu = get_object_or_404(Ciudad, id_ciu=request.POST['fk_id_ciu'])
        propietario.save()
        return redirect('listar_propietarios')
    return render(request, 'editar_propietario.html', {'propietario': propietario, 'ciudades': Ciudad.objects.all()})

def eliminar_propietario(request, id_pro):
    propietario = get_object_or_404(Propietario, id_pro=id_pro)
    propietario.delete()
    return redirect('listar_propietarios')

# CRUD para Vehiculo
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'listar_vehiculos.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    if request.method == 'POST':
        fabricacion_veh = request.POST['fabricacion_veh']
        precio_veh = request.POST['precio_veh']
        color_veh = request.POST['color_veh']
        placa_veh = request.POST['placa_veh']
        fk_id_mod = get_object_or_404(Modelo, id_mod=request.POST['fk_id_mod'])
        fk_id_pro = get_object_or_404(Propietario, id_pro=request.POST['fk_id_pro'])
        Vehiculo.objects.create(
            fabricacion_veh=fabricacion_veh, precio_veh=precio_veh,
            color_veh=color_veh, placa_veh=placa_veh,
            fk_id_mod=fk_id_mod, fk_id_pro=fk_id_pro
        )
        return redirect('listar_vehiculos')
    return render(request, 'crear_vehiculo.html', {
        'modelos': Modelo.objects.all(), 'propietarios': Propietario.objects.all()
    })

def editar_vehiculo(request, id_veh):
    vehiculo = get_object_or_404(Vehiculo, id_veh=id_veh)
    if request.method == 'POST':
        vehiculo.fabricacion_veh = request.POST['fabricacion_veh']
        vehiculo.precio_veh = request.POST['precio_veh']
        vehiculo.color_veh = request.POST['color_veh']
        vehiculo.placa_veh = request.POST['placa_veh']
        vehiculo.fk_id_mod = get_object_or_404(Modelo, id_mod=request.POST['fk_id_mod'])
        vehiculo.fk_id_pro = get_object_or_404(Propietario, id_pro=request.POST['fk_id_pro'])
        vehiculo.save()
        return redirect('listar_vehiculos')
    return render(request, 'editar_vehiculo.html', {
        'vehiculo': vehiculo, 'modelos': Modelo.objects.all(), 'propietarios': Propietario.objects.all()
    })

def eliminar_vehiculo(request, id_veh):
    vehiculo = get_object_or_404(Vehiculo, id_veh=id_veh)
    vehiculo.delete()
    return redirect('listar_vehiculos')



