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

    #----------------------------------------PERSONA-----------------------------------------------------------#
    path('Persona/', ListadoPersona.as_view(template_name = "crud\persona\index.html"), name='leerp'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro VER
    path('Persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "crud\persona\detalle.html"), name='detallep'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Persona/crear/', PersonaCrear.as_view(template_name = "crud\persona\crear.html"), name='crearp'), 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "crud/persona/actualizar.html"), name='actualizarp'), 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Persona/eliminar/<int:pk>', PersonaEliminar.as_view(template_name="crud\persona\eliminar.html"), name='Persona/eliminarp.html'),
    #----------------------------------------PERSONA-----------------------------------------------------------# 
               
    #----------------------------------------MASCOTA-----------------------------------------------------------#
    path('Mascota/', ListadoMascota.as_view(template_name = "crud\Mascota\index.html"), name='leerm'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Mascota/detalle/<int:pk>', MascotaDetalle.as_view(template_name = "crud\Mascota\detalle.html"), name='detallem'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Mascota/crear/', MascotaCrear.as_view(template_name = "crud\Mascota\crear.html"), name='crearm'), 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Mascota/editar/<int:pk>', MascotaActualizar.as_view(template_name = "crud/Mascota/actualizar.html"), name='actualizarm'), 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Mascota/eliminar/<int:pk>', MascotaEliminar.as_view(template_name="crud/Mascota/eliminar.html"),name='crud\Mascota\eliminarm.html'),
    #----------------------------------------MASCOTA-----------------------------------------------------------#   
    
    #----------------------------------------EMPRESA-----------------------------------------------------------#
    path('Empresa/', ListadoEmpresa.as_view(template_name = "crud\Empresa\index.html"), name='leere'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Empresa/detalle/<int:pk>', EmpresaDetalle.as_view(template_name = "crud\Empresa\detalle.html"), name='detallee'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Empresa/crear/', EmpresaCrear.as_view(template_name = "crud\Empresa\crear.html"), name='creare'), 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Empresa/editar/<int:pk>', EmpresaActualizar.as_view(template_name = "crud/Empresa/actualizar.html"), name='actualizare'), 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Empresa/eliminar/<int:pk>', EmpresaEliminar.as_view(template_name="crud/Empresa/eliminar.html"),name='crud\Empresa\eliminare.html'),
    #----------------------------------------EMPRESA-----------------------------------------------------------#   
      
    #----------------------------------------COLLAR-----------------------------------------------------------#
    path('Collar/', ListadoCollar.as_view(template_name = "crud\collar\index.html"), name='leerco'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Collar/detalle/<int:pk>', CollarDetalle.as_view(template_name = "crud\collar\detalle.html"), name='detalleco'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Collar/crear/', CollarCrear.as_view(template_name = "crud\collar\crear.html"), name='crearco'), 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Collar/editar/<int:pk>', CollarActualizar.as_view(template_name = "crud/collar/actualizar.html"), name='actualizarco'), 
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Collar/eliminar/<int:pk>', CollarEliminar.as_view(template_name="crud/collar/eliminar.html"),name='crud\collar\eliminarco.html'),
    #----------------------------------------COLLAR-----------------------------------------------------------#   
    
    #----------------------------------------CLASE ALARMA-----------------------------------------------------------#
     path('Calarma/', ListadoCalarma.as_view(template_name = "crud\Calarma\index.html"), name='leerca'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Calarma/detalle/<int:pk>', CalarmaDetalle.as_view(template_name = "crud\Calarma\detalle.html"), name='detalleca'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Calarma/crear/', CalarmaCrear.as_view(template_name = "crud\Calarma\crear.html"), name='crearca'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Calarma/editar/<int:pk>', CalarmaActualizar.as_view(template_name = "crud\Calarma\actualizar.html"), name='actualizarca'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Calarma/eliminar/<int:pk>', CalarmaEliminar.as_view(template_name="crud\Calarma\eliminar.html"), name='calarma\eliminarco.html'),
    #----------------------------------------CLASE ALARMA-----------------------------------------------------------#
    
    #----------------------------------------ALARMA-----------------------------------------------------------#
     path('Alarma/', ListadoAlarma.as_view(template_name = "crud\Alarma\index.html"), name='leera'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Alarma/detalle/<int:pk>', AlarmaDetalle.as_view(template_name = "crud\Alarma\detalle.html"), name='detallea'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Alarma/crear/', AlarmaCrear.as_view(template_name = "crud\Alarma\crear.html"), name='creara'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Alarma/editar/<int:pk>', AlarmaActualizar.as_view(template_name = "crud\Alarma\Actualizar.html"), name='actualizara'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Alarma/eliminar/<int:pk>', AlarmaEliminar.as_view(template_name="crud\Alarma\eliminar.html"), name='alarma/eliminaa.html'),
    #----------------------------------------ALARMA-----------------------------------------------------------#
   
    #----------------------------------------HISTORIAL-----------------------------------------------------------#
    path('Historial/', ListadoHistorial.as_view(template_name = "crud\historial\index.html"), name='leerhi'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Historial/detalle/<int:pk>', HistorialDetalle.as_view(template_name = "crud\historial\detalle.html"), name='detallehi'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Historial/crear/',HistorialCrear.as_view(template_name = "crud\historial\crear.html"), name='crearhi'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Historial/editar/<int:pk>', HistorialActualizar.as_view(template_name = "crud\historial\Actualizar.html"), name='actualizarhi'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Historial/eliminar/<int:pk>', HistorialEliminar.as_view(template_name="crud\historial\eliminar.html"), name='crud\Historial\eliminarhi.html'),
    #----------------------------------------HISTORIAL-----------------------------------------------------------#
    
    #----------------------------------------TIPO DE ALARMAS-----------------------------------------------------------#
    path('Talarma/', ListadoTalarma.as_view(template_name = "crud\Talarma\index.html"), name='leerta'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Talarma/detalle/<int:pk>', TalarmaDetalle.as_view(template_name = "crud\Talarma\detalle.html"), name='detalleta'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Talarma/crear/',TalarmaCrear.as_view(template_name = "crud\Talarma\crear.html"), name='crearta'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Talarma/editar/<int:pk>', TalarmaActualizar.as_view(template_name = "crud\Talarma\Actualizar.html"), name='actualizarta'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Talarma/eliminar/<int:pk>', TalarmaEliminar.as_view(template_name="crud\Talarma\eliminar.html"), name='crud\Talarma\eliminarta.html'),
    #----------------------------------------TIPO DE ALARMAS-----------------------------------------------------------#

    #----------------------------------------INVENTARIO-----------------------------------------------------------#
    path('Inventario/', ListadoInventario.as_view(template_name = "crud\Inventario\index.html"), name='leerin'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Inventario/detalle/<int:pk>', InventarioDetalle.as_view(template_name = "crud\Inventario\detalle.html"), name='detallein'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Inventario/crear/',InventarioCrear.as_view(template_name = "crud\Inventario\crear.html"), name='crearin'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Inventario/editar/<int:pk>', InventarioActualizar.as_view(template_name = "crud\Inventario\Actualizar.html"), name='actualizarin'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Inventario/eliminar/<int:pk>', InventarioEliminar.as_view(template_name="crud\Inventario\eliminar.html"), name='crud\Inventario\eliminarin.html'),
    #----------------------------------------INVENTARIO-----------------------------------------------------------#

    #----------------------------------------GEOLOCALIZACION-----------------------------------------------------------#
    path('Geolocalizacion/', ListadoGeolocalizacion.as_view(template_name = "crud\Geolocalizacion\index.html"), name='leergeo'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Geolocalizacion/detalle/<int:pk>', GeolocalizacionDetalle.as_view(template_name = "crud\Geolocalizacion\detalle.html"), name='detallegeo'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Geolocalizacion/crear/',GeolocalizacionCrear.as_view(template_name = "crud\Geolocalizacion\crear.html"), name='creargeo'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Geolocalizacion/editar/<int:pk>', GeolocalizacionActualizar.as_view(template_name = "crud\Geolocalizacion\Actualizar.html"), name='actualizargeo'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Geolocalizacion/eliminar/<int:pk>', GeolocalizacionEliminar.as_view(template_name="crud\Geolocalizacion\eliminar.html"), name='crud\Geolocalizacion\eliminargeo.html'),
    #----------------------------------------GEOLOCALIZACION-----------------------------------------------------------#

    #----------------------------------------TIPODOCUMENTO-----------------------------------------------------------#
    path('Tdocumento/', ListadoTdocumento.as_view(template_name = "crud\Tdocumento\index.html"), name='leertd'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Tdocumento/detalle/<int:pk>', TdocumentoDetalle.as_view(template_name = "crud\Tdocumento\detalle.html"), name='detalletd'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Tdocumento/crear/',TdocumentoCrear.as_view(template_name = "crud\Tdocumento\crear.html"), name='creartd'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Tdocumento/editar/<int:pk>', TdocumentoActualizar.as_view(template_name = "crud\Tdocumento\Actualizar.html"), name='actualizartd'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Tdocumento/eliminar/<int:pk>', TdocumentoEliminar.as_view(template_name="crud\Tdocumento\eliminar.html"), name='crud\Tdocumento\eliminartd.html'),
    #----------------------------------------TIPODOCUMENTO-----------------------------------------------------------#

    #----------------------------------------TIPOPERSONA-----------------------------------------------------------#
    path('Tpersona/', ListadoTpersona.as_view(template_name = "crud\Tpersona\index.html"), name='leertp'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Tpersona/detalle/<int:pk>', TpersonaDetalle.as_view(template_name = "crud\Tpersona\detalle.html"), name='detalletp'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Tpersona/crear/',TpersonaCrear.as_view(template_name = "crud\Tpersona\crear.html"), name='creartp'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Tpersona/editar/<int:pk>', TpersonaActualizar.as_view(template_name = "crud\Tpersona\Actualizar.html"), name='actualizartp'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Tpersona/eliminar/<int:pk>', TpersonaEliminar.as_view(template_name="crud\Tpersona\eliminar.html"), name='crud\Tpersona\eliminartp.html'),
    #----------------------------------------TIPOPERSONA-----------------------------------------------------------#

    #----------------------------------------TIPOANIMAL-----------------------------------------------------------#
    path('Tanimal/', ListadoTanimal.as_view(template_name = "crud\Tanimal\index.html"), name='leerta'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Tanimal/detalle/<int:pk>', TanimalDetalle.as_view(template_name = "crud\Tanimal\detalle.html"), name='detalleta'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Tanimal/crear/',TanimalCrear.as_view(template_name = "crud\Tanimal\crear.html"), name='crearta'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Tanimal/editar/<int:pk>', TanimalActualizar.as_view(template_name = "crud\Tanimal\Actualizar.html"), name='actualizarta'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Tanimal/eliminar/<int:pk>', TanimalEliminar.as_view(template_name="crud\Tanimal\eliminar.html"), name='crud\Tanimal\eliminarta.html'),
    #----------------------------------------TIPOANIMAL-----------------------------------------------------------#

    #----------------------------------------RAZA-----------------------------------------------------------#
    path('Raza/', ListadoRaza.as_view(template_name = "crud\Raza\index.html"), name='leerra'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Raza/detalle/<int:pk>', RazaDetalle.as_view(template_name = "crud\Raza\detalle.html"), name='detallera'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Raza/crear/',RazaCrear.as_view(template_name = "crud\Raza\crear.html"), name='crearra'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Raza/editar/<int:pk>', RazaActualizar.as_view(template_name = "crud\Raza\Actualizar.html"), name='actualizarra'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Raza/eliminar/<int:pk>', RazaEliminar.as_view(template_name="crud\Raza\eliminar.html"), name='crud\Raza\eliminarra.html'),
    #----------------------------------------RAZA-----------------------------------------------------------#

    #----------------------------------------ESPECIE-----------------------------------------------------------#
    path('Especie/', ListadoEspecie.as_view(template_name = "crud\Especie\index.html"), name='leeres'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Especie/detalle/<int:pk>', EspecieDetalle.as_view(template_name = "crud\Especie\detalle.html"), name='detallees'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Especie/crear/',EspecieCrear.as_view(template_name = "crud\Especie\crear.html"), name='crearra'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Especie/editar/<int:pk>', EspecieActualizar.as_view(template_name = "crud\Especie\Actualizar.html"), name='actualizares'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Especie/eliminar/<int:pk>', EspecieEliminar.as_view(template_name="crud\Especie\eliminar.html"), name='crud\Especie\eliminares.html'),
    #----------------------------------------ESPECIE-----------------------------------------------------------#

    #----------------------------------------EVENTO-----------------------------------------------------------#
    path('Evento/', ListadoEvento.as_view(template_name = "crud\Evento\index.html"), name='leerev'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Evento/detalle/<int:pk>', EventoDetalle.as_view(template_name = "crud\Evento\detalle.html"), name='detalleev'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Evento/crear/',EventoCrear.as_view(template_name = "crud\Evento\crear.html"), name='crearev'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Evento/editar/<int:pk>', EventoActualizar.as_view(template_name = "crud\Evento\Actualizar.html"), name='actualizarev'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Evento/eliminar/<int:pk>', EventoEliminar.as_view(template_name="crud\Evento\eliminar.html"), name='crud\Evento\eliminarev.html'),
    #----------------------------------------EVENTO-----------------------------------------------------------#

    #----------------------------------------FCABEZA-----------------------------------------------------------#
    path('Fcabeza/', ListadoFcabeza.as_view(template_name = "crud\Fcabeza\index.html"), name='leerfc'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Fcabeza/detalle/<int:pk>', FcabezaDetalle.as_view(template_name = "crud\Fcabeza\detalle.html"), name='detallefc'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Fcabeza/crear/',FcabezaCrear.as_view(template_name = "crud\Fcabeza\crear.html"), name='crearfc'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Fcabeza/editar/<int:pk>', FcabezaActualizar.as_view(template_name = "crud\Fcabeza\Actualizar.html"), name='actualizarfc'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Fcabeza/eliminar/<int:pk>', FcabezaEliminar.as_view(template_name="crud\Fcabeza\eliminar.html"), name='crud\Fcabeza\eliminarfc.html'),
    #----------------------------------------FCABEZA-----------------------------------------------------------#

    #----------------------------------------FCUERPO-----------------------------------------------------------#
    path('Fcuerpo/', ListadoFcuerpo.as_view(template_name = "crud\Fcuerpo\index.html"), name='leerfcu'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Fcuerpo/detalle/<int:pk>', FcuerpoDetalle.as_view(template_name = "crud\Fcuerpo\detalle.html"), name='detallefcu'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Fcuerpo/crear/',FcuerpoCrear.as_view(template_name = "crud\Fcuerpo\crear.html"), name='crearfcu'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Fcuerpo/editar/<int:pk>', FcuerpoActualizar.as_view(template_name = "crud\Fcuerpo\Actualizar.html"), name='actualizarfcu'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Fcuerpo/eliminar/<int:pk>', FcuerpoEliminar.as_view(template_name="crud\Fcuerpo\eliminar.html"), name='crud\Fcuerpo\eliminarfcu.html'),
    #----------------------------------------FCUERPO-----------------------------------------------------------#

    #----------------------------------------RELACION-----------------------------------------------------------#
    path('Relacion/', ListadoRelacion.as_view(template_name = "crud\Relacion\index.html"), name='leerrel'),
    # La ruta 'detalles' en donde mostraremos una página con los detalles de una mascota o registro 
    path('Relacion/detalle/<int:pk>', RelacionDetalle.as_view(template_name = "crud\Relacion\detalle.html"), name='detallerel'),
    # La ruta 'crear' en donde mostraremos un formulario para crear un nueva mascota o registro  
    path('Relacion/crear/',RelacionCrear.as_view(template_name = "crud\Relacion\crear.html"), name='crearrel'),
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar una mascota o registro de la Base de Datos 
    path('Relacion/editar/<int:pk>', RelacionActualizar.as_view(template_name = "crud\Relacion\Actualizar.html"), name='actualizarrel'),
    # La ruta 'eliminar' que usaremos para eliminar una mascota o registro de la Base de Datos 
    path('Relacion/eliminar/<int:pk>', RelacionEliminar.as_view(template_name="crud\Relacion\eliminar.html"), name='crud\Relacion\eliminarrel.html'),
    #----------------------------------------RELACION-----------------------------------------------------------#

]



    
