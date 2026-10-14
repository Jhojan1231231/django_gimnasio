from django.contrib import admin
from .models import plan, socio

admin.site.register(plan)
class planAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'duracion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('duracion',)

admin.site.register(socio)
class socioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'plan', 'mensualidad')
    search_fields = ('plan__nombre', 'nombre', 'apellido', 'email')
    list_filter = ('plan',)
    
admin.display(description='mensualidad')
def mensualidad(self, obj):
    monto = f"{obj.mensualidad:.2f}".replace(',', '.')
    return monto