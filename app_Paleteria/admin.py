from django.contrib import admin
from .models import Proveedor, Producto, Cliente

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre_empresa', 'telefono', 'email', 'ciudad', 'fecha_registro')
    search_fields = ('nombre_empresa', 'ciudad')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'sabor', 'precio', 'stock', 'tipo', 'id_proveedor')
    search_fields = ('nombre', 'sabor', 'tipo')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'apellido', 'telefono', 'email', 'direccion', 'id_producto', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'telefono', 'email')
