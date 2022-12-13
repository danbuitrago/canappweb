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
               
    #----------------------------------------Collar-----------------------------------------------------------#
    path('Collar/', ListadoCollar.as_view(template_name = "crud\collar\index.html"), name='leerco'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Collar/detalle/<int:pk>', CollarDetalle.as_view(template_name = "crud\collar\detalle.html"), name='detalleco'),
    

    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Collar/crear/', CollarCrear.as_view(template_name = "crud\collar\crear.html"), name='crearco'),
    
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Collar/editar/<int:pk>', CollarActualizar.as_view(template_name = "crud/collar/actualizar.html"), name='actualizarco'),
    
 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Collar/eliminar/<int:pk>', CollarEliminar.as_view(),name='crud\collar\eliminar.html'),

    #----------------------------------------Collar-----------------------------------------------------------#    
    # 
      
               
         #----------------------------------------Persona-----------------------------------------------------------#
     path('Persona/', ListadoPersona.as_view(template_name = "crud\persona\index.html"), name='leerp'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "crud\persona\detalle.html"), name='detallep'),
    

    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Persona/crear/', PersonaCrear.as_view(template_name = "crud\persona\crear.html"), name='crearp'),
    
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "crud\persona\actualizar.html"), name='actualizarp'),
    
 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Persona/eliminar/<int:pk>', PersonaEliminar.as_view(template_name="crud\persona\eliminar.html"), name='Persona/eliminarp.html'),

    #----------------------------------------Persona-----------------------------------------------------------#
            
               
               
               
               
               
               
               
               
               
               
               
               
               
               
   
    path('mascota/', ListadoMascota.as_view(template_name = "crud\mascota\index.html"), name='leerm'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('mascota/detalle/<int:pk>', MascotaDetalle.as_view(template_name = "crud\mascota\detalle.html"), name='detallem'),
    

    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('mascota/crear/', MascotaCrear.as_view(template_name = "crud\mascota\crear.html"), name='crearm'),
    
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('mascota/editar/<int:pk>', MascotaActualizar.as_view(template_name = "crud\mascota\ctualizar.html"), name='actualizarm'),
    
 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('mascota/eliminar/<int:pk>', MascotaEliminar.as_view(template_name="crud\mascota\eliminar.html"), name='mascota/eliminarm.html'),




  #----------------------------------------Persona-----------------------------------------------------------#
     path('Persona/', ListadoPersona.as_view(template_name = "crud\persona\index.html"), name='leerp'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "crud\persona\detalle.html"), name='detallep'),
    

    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Persona/crear/', PersonaCrear.as_view(template_name = "crud\persona\crear.html"), name='crearp'),
    
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "crud\persona\Actualizar.html"), name='actualizarp'),
    
 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Persona/eliminar/<int:pk>', PersonaEliminar.as_view(template_name="crud\persona\eliminar.html"), name='Persona/eliminarp.html'),

    #----------------------------------------Persona-----------------------------------------------------------#
      

    #----------------------------------------EMPRESA-----------------------------------------------------------#
    #----------------------------------------EMPRESA-----------------------------------------------------------#
     path('empresa/', ListadoEmpresa.as_view(template_name = "crud\empresa\index.html"), name='leere'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('empresa/detalle/<int:pk>', EmpresaDetalle.as_view(template_name = "crud\empresa\detalle.html"), name='detallee'),
    

    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('empresa/crear/', EmpresaCrear.as_view(template_name = "crud\empresa\crear.html"), name='creare'),
    
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('empresa/editar/<int:pk>', EmpresaActualizar.as_view(template_name = "crud\empresa\Actualizar.html"), name='actualizare'),
    
 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('empresa/eliminar/<int:pk>', EmpresaEliminar.as_view(template_name="crud\empresa\eliminar.html"), name='empresa/eliminare.html'),

    #----------------------------------------EMPRESA-----------------------------------------------------------#
    #----------------------------------------EMPRESA-----------------------------------------------------------#
    
    
    
    #----------------------------------------Clase alarma-----------------------------------------------------------#
     path('Calarma/', ListadoCalarma.as_view(template_name = "crud\Calarma\index.html"), name='leerca'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Calarma/detalle/<int:pk>', CalarmaDetalle.as_view(template_name = "crud\Calarma\detalle.html"), name='detalleca'),
    

    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Calarma/crear/', CalarmaCrear.as_view(template_name = "crud\Calarma\crear.html"), name='crearca'),
    
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Calarma/editar/<int:pk>', CalarmaActualizar.as_view(template_name = "crud\Calarma\actualizar.html"), name='actualizarca'),
    
 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Calarma/eliminar/<int:pk>', CalarmaEliminar.as_view(template_name="crud\Calarma\eliminar.html"), name='Calarma/eliminaca.html'),

    #----------------------------------------Clase alarma-----------------------------------------------------------#
    
    
#----------------------------------------Alarma-----------------------------------------------------------#
#----------------------------------------Alarma-----------------------------------------------------------#
#----------------------------------------Alarma-----------------------------------------------------------#
#----------------------------------------Alarma-----------------------------------------------------------#
#----------------------------------------Alarma-----------------------------------------------------------#
     path('Alarma/', ListadoAlarma.as_view(template_name = "crud\Alarma\index.html"), name='leera'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Alarma/detalle/<int:pk>', AlarmaDetalle.as_view(template_name = "crud\Alarma\detalle.html"), name='detallea'),
    

    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Alarma/crear/', AlarmaCrear.as_view(template_name = "crud\Alarma\crear.html"), name='creara'),
    
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Alarma/editar/<int:pk>', AlarmaActualizar.as_view(template_name = "crud\Alarma\Actualizar.html"), name='actualizara'),
    
 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Alarma/eliminar/<int:pk>', AlarmaEliminar.as_view(template_name="crud\Alarma\eliminar.html"), name='alarma/eliminaa.html'),

#----------------------------------------Alarma-----------------------------------------------------------#
#----------------------------------------Alarma-----------------------------------------------------------#
#----------------------------------------Alarma-----------------------------------------------------------#
#----------------------------------------Alarma-----------------------------------------------------------#
#----------------------------------------Alarma-----------------------------------------------------------#

   
    
    
   
    
      
]



    
