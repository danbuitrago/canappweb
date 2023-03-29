from django.contrib import admin
from .models import Service         # se importa Service desde models de esta app

# Configuracion especial de la app Service 
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')               #campos solo de lectura
#registro de la app Service y su contenido especial
admin.site.register(Service, ServiceAdmin)
