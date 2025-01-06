from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ciudad,Modelo, Propietario, Ciudad,Vehiculo
from django.contrib import messages

# Crear vista principal
def home(request):
    return render(request, 'home.html')

# CRUD para Ciudad
def listar_ciudades(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'listar_ciudades.html', {'ciudades': ciudades})

# Función de validación en el backend
def validar_nombre_ciudad(nombre_ciu):
    if not re.match("^[A-Za-zÁáÉéÍíÓóÚúÑñ ]+$", nombre_ciu):
        raise ValidationError("El nombre de la ciudad solo puede contener letras y espacios.")

def crear_ciudad(request):
    if request.method == 'POST':
        nombre_ciu = request.POST['nombre_ciu']
        try:
            # Validación en el backend
            validar_nombre_ciudad(nombre_ciu)
            Ciudad.objects.create(nombre_ciu=nombre_ciu)
            messages.success(request, "Ciudad creada exitosamente.")
            return redirect('listar_ciudades')
        except ValidationError as e:
            messages.error(request, e.message)
            return redirect('crear_ciudad')  # Redirige de nuevo al formulario
    return render(request, 'crear_ciudad.html')

# Vista para editar ciudad
def editar_ciudad(request, id_ciu):
    ciudad = get_object_or_404(Ciudad, id_ciu=id_ciu)
    if request.method == 'POST':
        nombre_ciu = request.POST['nombre_ciu']
        try:
            # Validación en el backend
            validar_nombre_ciudad(nombre_ciu)
            ciudad.nombre_ciu = nombre_ciu
            ciudad.save()
            messages.success(request, "Ciudad actualizada exitosamente.")
            return redirect('listar_ciudades')
        except ValidationError as e:
            messages.error(request, e.message)
            return redirect('editar_ciudad', id_ciu=id_ciu)  # Redirige de nuevo al formulario
    return render(request, 'editar_ciudad.html', {'ciudad': ciudad})


def eliminar_ciudad(request, id_ciu):
    ciudad = get_object_or_404(Ciudad, id_ciu=id_ciu)
    ciudad.delete()
    messages.success(request, "Ciudad eliminada exitosamente.")
    return redirect('listar_ciudades')

# CRUD para Modelo
def listar_modelos(request):
    modelos = Modelo.objects.all()
    return render(request, 'listar_modelos.html', {'modelos': modelos})

def crear_modelo(request):
    if request.method == 'POST':
        nombre_mod = request.POST['nombre_mod']
        
        # Validación para asegurar que el nombre no exceda los 20 caracteres
        if len(nombre_mod) > 20:
            messages.error(request, "El nombre del modelo no puede exceder los 20 caracteres.")
            return redirect('crear_modelo')

        Modelo.objects.create(nombre_mod=nombre_mod)
        messages.success(request, "Modelo creado exitosamente.")
        return redirect('listar_modelos')
    return render(request, 'crear_modelo.html')


def editar_modelo(request, id_mod):
    modelo = get_object_or_404(Modelo, id_mod=id_mod)
    if request.method == 'POST':
        nombre_mod = request.POST['nombre_mod']
        
        # Validación para asegurar que el nombre no exceda los 20 caracteres
        if len(nombre_mod) > 20:
            messages.error(request, "El nombre del modelo no puede exceder los 20 caracteres.")
            return redirect('editar_modelo', id_mod=id_mod)

        modelo.nombre_mod = nombre_mod
        modelo.save()
        messages.success(request, "Modelo actualizado exitosamente.")
        return redirect('listar_modelos')
    return render(request, 'editar_modelo.html', {'modelo': modelo})


def eliminar_modelo(request, id_mod):
    modelo = get_object_or_404(Modelo, id_mod=id_mod)
    modelo.delete()
    messages.success(request, "Modelo eliminado exitosamente.")
    return redirect('listar_modelos')



# Función de validación para asegurarse de que solo contenga letras
def validar_nombre_apellido(valor):
    if not re.match("^[A-Za-zÁáÉéÍíÓóÚúÑñ ]+$", valor):
        raise ValidationError("Este campo solo puede contener letras y espacios.")
    
# CRUD para Propietario
def listar_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'listar_propietarios.html', {'propietarios': propietarios})

# Función de creación de propietario
def crear_propietario(request):
    if request.method == 'POST':
        nombre_pro = request.POST['nombre_pro']
        apellido_pro = request.POST['apellido_pro']
        email_pro = request.POST['email_pro']
        telefono_pro = request.POST['telefono_pro']
        fk_id_ciu = get_object_or_404(Ciudad, id_ciu=request.POST['fk_id_ciu'])
        
        try:
            # Validación en el backend para nombre y apellido
            validar_nombre_apellido(nombre_pro)
            validar_nombre_apellido(apellido_pro)
            
            Propietario.objects.create(
                nombre_pro=nombre_pro, apellido_pro=apellido_pro,
                email_pro=email_pro, telefono_pro=telefono_pro, fk_id_ciu=fk_id_ciu
            )
            messages.success(request, "Propietario creado exitosamente.")
            return redirect('listar_propietarios')
        except ValidationError as e:
            messages.error(request, e.message)
            return redirect('crear_propietario')  # Redirige de nuevo al formulario
    
    return render(request, 'crear_propietario.html', {'ciudades': Ciudad.objects.all()})

# Función para editar propietario
def editar_propietario(request, id_pro):
    propietario = get_object_or_404(Propietario, id_pro=id_pro)
    if request.method == 'POST':
        nombre_pro = request.POST['nombre_pro']
        apellido_pro = request.POST['apellido_pro']
        email_pro = request.POST['email_pro']
        telefono_pro = request.POST['telefono_pro']
        fk_id_ciu = get_object_or_404(Ciudad, id_ciu=request.POST['fk_id_ciu'])

        try:
            # Validación en el backend para nombre y apellido
            validar_nombre_apellido(nombre_pro)
            validar_nombre_apellido(apellido_pro)
            
            propietario.nombre_pro = nombre_pro
            propietario.apellido_pro = apellido_pro
            propietario.email_pro = email_pro
            propietario.telefono_pro = telefono_pro
            propietario.fk_id_ciu = fk_id_ciu
            propietario.save()
            
            messages.success(request, "Propietario actualizado exitosamente.")
            return redirect('listar_propietarios')
        except ValidationError as e:
            messages.error(request, e.message)
            return redirect('editar_propietario', id_pro=id_pro)  # Redirige de nuevo al formulario
    
    return render(request, 'editar_propietario.html', {
        'propietario': propietario, 'ciudades': Ciudad.objects.all()
    })

def eliminar_propietario(request, id_pro):
    propietario = get_object_or_404(Propietario, id_pro=id_pro)
    propietario.delete()
    messages.success(request, "Propietario eliminado exitosamente.")
    return redirect('listar_propietarios')



# Validación para el año de fabricación (solo números, máximo 4 dígitos)
def validar_fabricacion_veh(fabricacion_veh):
    if not re.match("^\d{4}$", fabricacion_veh):
        raise ValidationError("El año de fabricación debe ser un número de 4 dígitos.")

# Validación para el color (solo letras, máximo 20 caracteres)
def validar_color_veh(color_veh):
    if not re.match("^[A-Za-zÁáÉéÍíÓóÚúÑñ ]+$", color_veh):
        raise ValidationError("El color solo puede contener letras y espacios.")
    if len(color_veh) > 20:
        raise ValidationError("El color no puede exceder los 20 caracteres.")

# Validación para el propietario (solo letras, máximo 20 caracteres)
def validar_propietario(propietario):
    if not re.match("^[A-Za-zÁáÉéÍíÓóÚúÑñ ]+$", propietario):
        raise ValidationError("El nombre del propietario solo puede contener letras y espacios.")
    if len(propietario) > 20:
        raise ValidationError("El nombre del propietario no puede exceder los 20 caracteres.")

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

        try:
            # Validaciones
            validar_fabricacion_veh(fabricacion_veh)
            validar_color_veh(color_veh)
            validar_propietario(fk_id_pro.nombre_pro)

            Vehiculo.objects.create(
                fabricacion_veh=fabricacion_veh, precio_veh=precio_veh,
                color_veh=color_veh, placa_veh=placa_veh,
                fk_id_mod=fk_id_mod, fk_id_pro=fk_id_pro
            )
            messages.success(request, "Vehículo creado exitosamente.")
            return redirect('listar_vehiculos')
        except ValidationError as e:
            messages.error(request, e.message)
            return redirect('crear_vehiculo')  # Redirige de nuevo al formulario

    return render(request, 'crear_vehiculo.html', {
        'modelos': Modelo.objects.all(), 'propietarios': Propietario.objects.all()
    })


def editar_vehiculo(request, id_veh):
    vehiculo = get_object_or_404(Vehiculo, id_veh=id_veh)
    if request.method == 'POST':
        fabricacion_veh = request.POST['fabricacion_veh']
        precio_veh = request.POST['precio_veh']
        color_veh = request.POST['color_veh']
        placa_veh = request.POST['placa_veh']
        fk_id_mod = get_object_or_404(Modelo, id_mod=request.POST['fk_id_mod'])
        fk_id_pro = get_object_or_404(Propietario, id_pro=request.POST['fk_id_pro'])

        try:
            # Validaciones
            validar_fabricacion_veh(fabricacion_veh)
            validar_color_veh(color_veh)
            validar_propietario(fk_id_pro.nombre_pro)

            vehiculo.fabricacion_veh = fabricacion_veh
            vehiculo.precio_veh = precio_veh
            vehiculo.color_veh = color_veh
            vehiculo.placa_veh = placa_veh
            vehiculo.fk_id_mod = fk_id_mod
            vehiculo.fk_id_pro = fk_id_pro
            vehiculo.save()

            messages.success(request, "Vehículo actualizado exitosamente.")
            return redirect('listar_vehiculos')
        except ValidationError as e:
            messages.error(request, e.message)
            return redirect('editar_vehiculo', id_veh=id_veh)  # Redirige de nuevo al formulario

    return render(request, 'editar_vehiculo.html', {
        'vehiculo': vehiculo, 'modelos': Modelo.objects.all(), 'propietarios': Propietario.objects.all()
    })



def eliminar_vehiculo(request, id_veh):
    vehiculo = get_object_or_404(Vehiculo, id_veh=id_veh)
    vehiculo.delete()
    messages.success(request, "Vehículo eliminado exitosamente.")
    return redirect('listar_vehiculos')
