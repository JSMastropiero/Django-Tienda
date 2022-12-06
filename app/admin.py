from django.contrib import admin
from .models import Marca, Producto,Contacto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    list_editable = ["precio"]  #Hago que sólo la columna precio sea editable
    search_fields = ["nombre"]
    list_filter = ["nuevo", "marca"]
    list_per_page = 5

admin.site.register(Marca)  ##Creamos los campos para el panel  del admin
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)
