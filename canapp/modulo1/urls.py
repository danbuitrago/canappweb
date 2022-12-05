"""canapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # se importa include
from modulo1.views import*

urlpatterns = [ 
   
path('mascota/', ListadoMascota.as_view(template_name = "crud\mascota\index.html"), name='leerm'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('mascota/detalle/<int:pk>', MascotaDetalle.as_view(template_name = "crud\mascota\detalle.html"), name='detallem'),
    

    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('mascota/crear/', MascotaCrear.as_view(template_name = "crud\mascota\crear.html"), name='crearm'),
    
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('mascota/editar/<int:pk>', MascotaActualizar.as_view(template_name = "crud\mascota\actualizar.html"), name='actualizarm'),
    
 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('mascota/eliminar/<int:pk>', MascotaEliminar.as_view(template_name="crud\mascota\eliminar.html"), name='mascota/eliminarm.html'),


    
    
    path('persona/', ListadoPersona.as_view(template_name = "crud\persona\index.html"), name='leerp'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "crud\persona\detalle.html"), name='detallep'),
    

    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('persona/crear/', PersonaCrear.as_view(template_name = "crud\persona\crear.html"), name='crearp'),
    
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "crud\persona\actualizar.html"), name='actualizarp'),
    
 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Persona/eliminar/<int:pk>', PersonaEliminar.as_view(template_name="crud\persona\eliminar.html"), name='persona/eliminarp.html'),
      
]



    
