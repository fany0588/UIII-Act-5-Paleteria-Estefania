from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor, Cliente
from django.utils import timezone

# =====================================
# INICIO
# =====================================
def inicio_paleteria(request):
    return render(request, 'inicio.html')


# =====================================
# CRUD PROVEEDOR
# =====================================
def agregar_proveedor(request):
    if request.method == 'POST':
        nombre_empresa = request.POST.get('nombre_empresa', '')
        contacto = request.POST.get('contacto', '')
        telefono = request.POST.get('telefono', '')
        email = request.POST.get('email', '')
        direccion = request.POST.get('direccion', '')
        ciudad = request.POST.get('ciudad', '')
        Proveedor.objects.create(
            nombre_empresa=nombre_empresa,
            contacto=contacto,
            telefono=telefono,
            email=email,
            direccion=direccion,
            ciudad=ciudad,
            fecha_registro=timezone.now().date()
        )
        return redirect('ver_proveedor')
    return render(request, 'proveedor/agregar_proveedor.html')


def ver_proveedor(request):
    proveedores = Proveedor.objects.all().order_by('id_proveedor')
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})


def actualizar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})


def realizar_actualizacion_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.nombre_empresa = request.POST.get('nombre_empresa', proveedor.nombre_empresa)
        proveedor.contacto = request.POST.get('contacto', proveedor.contacto)
        proveedor.telefono = request.POST.get('telefono', proveedor.telefono)
        proveedor.email = request.POST.get('email', proveedor.email)
        proveedor.direccion = request.POST.get('direccion', proveedor.direccion)
        proveedor.ciudad = request.POST.get('ciudad', proveedor.ciudad)
        proveedor.save()
        return redirect('ver_proveedor')
    return redirect('ver_proveedor')


def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})


# =====================================
# CRUD PRODUCTO
# =====================================
def agregar_producto(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        sabor = request.POST['sabor']
        precio = request.POST['precio']
        stock = request.POST['stock']
        tipo = request.POST['tipo']
        fecha_elaboracion = request.POST['fecha_elaboracion']
        id_proveedor = request.POST['id_proveedor']

        proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
        Producto.objects.create(
            nombre=nombre, sabor=sabor, precio=precio,
            stock=stock, tipo=tipo, fecha_elaboracion=fecha_elaboracion,
            id_proveedor=proveedor
        )
        return redirect('ver_producto')
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/agregar_producto.html', {'proveedores': proveedores})


def ver_producto(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_producto.html', {'productos': productos})


def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    proveedores = Proveedor.objects.all()
    return render(request, 'producto/actualizar_producto.html', {'producto': producto, 'proveedores': proveedores})


def realizar_actualizacion_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == "POST":
        producto.nombre = request.POST['nombre']
        producto.sabor = request.POST['sabor']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.tipo = request.POST['tipo']
        producto.fecha_elaboracion = request.POST['fecha_elaboracion']
        id_proveedor = request.POST['id_proveedor']
        producto.id_proveedor = Proveedor.objects.get(id_proveedor=id_proveedor)
        producto.save()
        return redirect('ver_producto')
    return redirect('ver_producto')


def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    producto.delete()
    return redirect('ver_producto')



# =====================================
# CRUD CLIENTE
# =====================================

def agregar_cliente(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        email = request.POST['email']
        direccion = request.POST['direccion']
        fecha_registro = timezone.now().date()
        id_producto = request.POST['id_producto']

        producto = Producto.objects.get(id_producto=id_producto)
        Cliente.objects.create(
            nombre=nombre, apellido=apellido, telefono=telefono,
            email=email, direccion=direccion, fecha_registro=fecha_registro,
            id_producto=producto
        )
        return redirect('ver_cliente')
    productos = Producto.objects.all()
    return render(request, 'cliente/agregar_cliente.html', {'productos': productos})


def ver_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})


def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    productos = Producto.objects.all()
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente, 'productos': productos})


def realizar_actualizacion_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    if request.method == "POST":
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST['email']
        cliente.direccion = request.POST['direccion']
        id_producto = request.POST['id_producto']
        cliente.id_producto = Producto.objects.get(id_producto=id_producto)
        cliente.save()
        return redirect('ver_cliente')
    return redirect('ver_cliente')


def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    cliente.delete()
    return redirect('ver_cliente')
