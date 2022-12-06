from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages 
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

#login_required lo usamos para que solo si esta logeado pueda ver alguna pagina, pero no necesita de permisos. Es una funcionalidad un poco más básica.

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data={
        'productos' : productos
    }

    return render(request, 'app/home.html', data)

def contacto(request):
    data={
        'form' : ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Formulario Enviado"
        else: 
            data["form"] = formulario

    return render(request,'app/contacto.html', data)    

def galeria(request):
    return render(request,'app/galeria.html')    

@permission_required('app.add_producto')
def agregar_producto(request):

    data = {
        'form' : ProductoForm()
    }

    if request.method == "POST":
        formulario = ProductoForm(data = request.POST, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Registrado")
        else:
            data["form"] = formulario
    return render(request, 'app/producto/agregar.html', data)
@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except: 
        raise Http404

    data = {
        'entity': productos, #usamos la palabra entity en vez de productos para poder reutilizar el código del paginador (paginator.html)
        'paginator':paginator
    }

    return render(request, 'app/producto/listar.html',data)
@permission_required('app.change_producto')
def modificar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)

    data={
        'form': ProductoForm(instance=producto)
    }
    if request.method == "POST":
        formulario = ProductoForm(data = request.POST,instance=producto, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario


    return render(request, 'app/producto/modificar.html', data)    
@permission_required('app.delete_producto')
def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_productos")


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"]) #password1 porque hay dos, la primera y la de confirmación.
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario    

    return render(request, 'registration/registro.html', data)
