from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Producto
from .forms import ProductoForm
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def listar(request):
    productos = Producto.objects.using('default').all()
    return render(request, 'listar_productos.html', {'productos':productos})

@login_required
def crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Revisar datos ingresados')
            return HttpResponseRedirect(reverse('crear_producto'))
    else:
        form = ProductoForm()
        return render(request, 'crear_producto.html', {'producto_form':form}) 
    
@login_required
def editar(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
    except Producto.DoesNotExist:
        messages.error(request, f"No se encontró un producto con ID {producto_id}.")
        return redirect('listar_producto')  

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado correctamente.')
            return redirect('listar_producto')
        else:
            messages.error(request, 'Datos inválidos para editar el producto.')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'producto_form': form, 'producto_id': producto_id})
 
@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    messages.success(request, 'Producto eliminado correctamente')
    return redirect('listar_producto')

def index(request):
    return render(request, 'index.html')


@login_required
def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        try:
            query_id = int(query)
        except ValueError:
            query_id = None
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | 
            Q(descripcion__icontains=query) | 
            (Q(id=query_id) if query_id is not None else Q())
            ).order_by('id')
        return render(request, 'listar_productos.html', {'productos':productos})


def mostrar_cadena(request, cadena):
    if not cadena.strip():
        return HttpResponse("El username está vacío o es inválido", status=400)
    return render(request, 'mostrar_cadena.html', {'cadena': cadena})
   
@login_required
def detalle_producto(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
    except Producto.DoesNotExist:
        messages.error(request, f"No se encontró un producto con ID {producto_id}.")
        return redirect('listar_producto')  # Redirect to product list
    return render(request, 'detalle_producto.html', {'producto': producto})


def crearusuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

                 # Autentica y loguea al usuario automáticamente
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registro exitoso y sesión iniciada')
                return redirect('index')
        else:
            print(form.errors)
            if 'username' in form.errors:
                messages.error(request, 'El nombre de usuario ya existe. Elige otro.')
            elif 'password2' in form.errors and any("didn't match" in str(error) for error in form.errors['password2']):
                messages.error(request, 'Los dos campos de contraseña no coinciden.')
            else:
                messages.error(request, 'Modifica los datos de ingreso.')
            return HttpResponseRedirect(reverse('crearusuario'))
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})
    
    
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificar las credenciales con authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Usar auth_login para iniciar sesión
            auth_login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect('listar_producto')  
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')

    return render(request, 'login.html') 

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('index')
    

