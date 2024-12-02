from django.contrib import admin
from .models import Fabrica, Producto

class ProductoInline(admin.TabularInline):  
    model = Producto
    extra = 1 
    fields = ('nombre', 'precio', 'descripcion', 'fecha_vencimiento') 


@admin.register(Fabrica)
class FabricaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais') 
    search_fields = ('nombre', 'pais')  
    list_filter = ('pais',) 
    inlines = [ProductoInline]  


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'costo', 'fecha_vencimiento', 'fabrica')  
    list_filter = ('fabrica', 'fecha_vencimiento') 
    search_fields = ('nombre', 'descripcion')  
    list_per_page = 5 
    
    def costo(self, obj):
        return "Costo Alto" if obj.precio >= 5000 else "Costo Bajo"
