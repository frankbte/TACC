from django.contrib import admin
from .models import Marca, Producto, Profile

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'nuevo', 'marca')
    list_editable = ('nuevo', 'precio')
    search_fields = ('nombre', 'precio')
    list_filter = ('marca', 'nuevo')


admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Profile)