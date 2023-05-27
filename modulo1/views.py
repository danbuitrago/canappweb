
# librerias del crud
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#importo el modelo de la base de datos de models.py
from .models import *
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms
# Importamos pqrs
#from .forms import ContactForm

# VISTA DE HOME
def Home(request):
    return render (request, "home.html")

# VISTA DE LOGIN
def Login(request):
    return render (request, "login.html")
# VISTA DE NOSOTROS
def Nosotros(request):
    return render (request, 'Nosotros.html')
# VISTA DE EMPRESA
def EmpresaInfo(request):
    return render (request, 'Empresa.html')
# VISTA DE UBICACION
def Ubicacion(request):
    return render (request, 'Ubicacion.html')


#-----------------------------COLLAR----------------------------------------------------#  
class ListadoCollar(ListView):
    model =Collar    
class CollarCrear(SuccessMessageMixin, CreateView):
    model = Collar
    form = Collar
    fields = "__all__"
    success_message ='Collar creada correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerco') # Redireccionamos a la vista principal 'leer' 
class CollarDetalle (DetailView):
    model =Collar 
class  CollarActualizar(SuccessMessageMixin,UpdateView):
    model =  Collar
    form = Collar
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Collar actualizada correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerco') # Redireccionamos a la vista principal 'leer'    
class CollarEliminar(SuccessMessageMixin, DeleteView): 
    model = Collar
    form = Collar
    fields = "__all__"   
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Collar eliminada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerco') # Redireccionamos a la vista principal 'leer'
#-----------------------------COLLAR----------------------------------------------------#  

#-----------------------------PERSONA----------------------------------------------------#     
class ListadoPersona(ListView):
    model = Persona   
class PersonaCrear(SuccessMessageMixin, CreateView):
    model = Persona
    form = Persona
    fields = "__all__"
    success_message ='Persona creada correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerp') # Redireccionamos a la vista principal 'leer' 
class PersonaDetalle (DetailView):
    model = Persona 
class  PersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Persona
    form = Persona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Persona Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerp') # Redireccionamos a la vista principal 'leer'
class PersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Persona 
    form = Persona
    fields = "__all__" 
# Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Persona Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerp') # Redireccionamos a la vista principal 'leer'
#-----------------------------PERSONA----------------------------------------------------#  

#-----------------------------MASCOTA----------------------------------------------------#  
class ListadoMascota(ListView):
    model = Mascota   
class MascotaCrear(SuccessMessageMixin, CreateView):
    model = Mascota
    form = Mascota
    fields = "__all__"
    success_message ='Mascota creada correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerm') # Redireccionamos a la vista principal 'leer' 
class MascotaDetalle (DetailView):
    model =Mascota 
class  MascotaActualizar(SuccessMessageMixin,UpdateView):
    model =  Mascota
    form = Mascota
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Mascota Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerm') # Redireccionamos a la vista principal 'leer'
class MascotaEliminar(SuccessMessageMixin, DeleteView): 
    model = Mascota 
    form = Mascota
    fields = "__all__"   
# Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Mascota Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerm') # Redireccionamos a la vista principal 'leer'
 #-----------------------------MASCOTA----------------------------------------------------#  

#-----------------------------EMPRESA----------------------------------------------------#  
class ListadoEmpresa(ListView):
    model = Empresa    
class EmpresaCrear(SuccessMessageMixin, CreateView):
    model = Empresa
    form = Empresa
    fields = "__all__"
    success_message ='Empresa creada correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leere') # Redireccionamos a la vista principal 'leer' 
class EmpresaDetalle (DetailView):
    model =Empresa 
class  EmpresaActualizar(SuccessMessageMixin,UpdateView):
    model =  Empresa
    form = Empresa
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Empresa Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leere') # Redireccionamos a la vista principal 'leer'
class EmpresaEliminar(SuccessMessageMixin, DeleteView): 
    model = Empresa
    form = Empresa
    fields = "__all__"      
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Empresa Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leere') # Redireccionamos a la vista principal 'leer'    
#-----------------------------EMPRESA----------------------------------------------------#  
  
#-----------------------------TIPO DE ANIMAL----------------------------------------------------#  
class ListadoTanimal(ListView):
    model = Tanimal    
class TanimalCrear(SuccessMessageMixin, CreateView):
    model = Tanimal
    form = Tanimal
    fields = "__all__"
    success_message ='Tipo animal creado correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerta') # Redireccionamos a la vista principal 'leer' 
class TanimalDetalle (DetailView):
    model =Tanimal 
class  TanimalActualizar(SuccessMessageMixin,UpdateView):
    model =  Tanimal
    form = Tanimal
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipo animal actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerta') # Redireccionamos a la vista principal 'leer'
class TanimalEliminar(SuccessMessageMixin, DeleteView): 
    model = Tanimal
    form = Tanimal
    fields = "__all__"      
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipo animal eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerta') # Redireccionamos a la vista principal 'leer'
#-----------------------------TIPO DE ANIMAL----------------------------------------------------# 

#-----------------------------RAZA----------------------------------------------------# 
class ListadoRaza(ListView):
    model =Raza    
class RazaCrear(SuccessMessageMixin, CreateView):
    model = Raza
    form = Raza
    fields = "__all__"
    success_message ='Raza creada correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerra') # Redireccionamos a la vista principal 'leer' 
class RazaDetalle (DetailView):
    model =Raza 
class  RazaActualizar(SuccessMessageMixin,UpdateView):
    model =  Raza
    form = Raza
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Raza actualizada correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerra') # Redireccionamos a la vista principal 'leer'
class RazaEliminar(SuccessMessageMixin, DeleteView): 
    model = Raza
    form = Raza
    fields = "__all__"      
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Raza eliminada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerra') # Redireccionamos a la vista principal 'leer'
#-----------------------------RAZA----------------------------------------------------# 

#-----------------------------ESPECIE----------------------------------------------------# 
class ListadoEspecie(ListView):
    model =Especie    
class EspecieCrear(SuccessMessageMixin, CreateView):
    model = Especie
    form = Especie
    fields = "__all__"
    success_message ='Especie creada correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leeres') # Redireccionamos a la vista principal 'leer' 
class EspecieDetalle (DetailView):
    model =Especie 
class  EspecieActualizar(SuccessMessageMixin,UpdateView):
    model =  Especie
    form = Especie
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Especie actualizada correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leeres') # Redireccionamos a la vista principal 'leer'
class EspecieEliminar(SuccessMessageMixin, DeleteView): 
    model = Especie
    form = Especie
    fields = "__all__"     
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Especie eliminada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leeres') # Redireccionamos a la vista principal 'leer'
#-----------------------------ESPECIE----------------------------------------------------# 

#-----------------------------TIPO PERSONA----------------------------------------------------#  
class ListadoTpersona(ListView):
    model =Tpersona    
class TpersonaCrear(SuccessMessageMixin, CreateView):
    model = Tpersona
    form = Tpersona
    fields = "__all__"
    success_message ='Tipo persona creada correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leertp') # Redireccionamos a la vista principal 'leer' 
class TpersonaDetalle (DetailView):
    model =Tpersona 
class TpersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tpersona
    form = Tpersona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipo persona actualizada correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leertp') # Redireccionamos a la vista principal 'leer'
class TpersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tpersona
    form = Tpersona
    fields = "__all__"      
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipo persona eliminada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertp') # Redireccionamos a la vista principal 'leer'
#-----------------------------TIPO PERSONA----------------------------------------------------#  

#-----------------------------TIPO DOCUMENTO----------------------------------------------------#  
class ListadoTdocumento(ListView):
    model =Tdocumento    
class TdocumentoCrear(SuccessMessageMixin, CreateView):
    model = Tdocumento
    form = Tdocumento
    fields = "__all__"
    success_message ='Tipo Documento creado correctamente'     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 
class TdocumentoDetalle (DetailView):
    model =Tdocumento 
class  TdocumentoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tdocumento
    form = Tdocumento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipo Documento actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class TdocumentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tdocumento
    form = Tdocumento
    fields = "__all__"      
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipo Documento eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
#-----------------------------TIPO DOCUMENTO----------------------------------------------------#  

#-----------------------------CLASE DE ALARMA----------------------------------------------------#   
class ListadoCalarma(ListView):
    model =Calarma    
class CalarmaCrear(SuccessMessageMixin, CreateView):
    model = Calarma
    form = Calarma
    fields = "__all__"
    success_message ='Clase alarma creada correctamente'     
    def get_success_url(self):        
        return reverse('leerca') # Redireccionamos a la vista principal 'leer' 
class CalarmaDetalle (DetailView):
    model =Calarma 
class  CalarmaActualizar(SuccessMessageMixin,UpdateView):
    model =  Calarma
    form = Calarma
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Clase alarma actualizada correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('leerca') # Redireccionamos a la vista principal 'leer'
class CalarmaEliminar(SuccessMessageMixin, DeleteView): 
    model = Calarma
    form = Calarma
    fields = "__all__"      
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Clase alarma eliminada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerca') # Redireccionamos a la vista principal 'leer'
#-----------------------------CLASE DE ALARMA----------------------------------------------------#   

#-----------------------------ALARMA----------------------------------------------------#   
class ListadoAlarma(ListView):
    model = Alarma   
class AlarmaCrear(SuccessMessageMixin, CreateView):
    model = Alarma
    form = Alarma
    fields = "__all__"
    success_message ='Alarma creada correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leera') # Redireccionamos a la vista principal 'leer' 
class AlarmaDetalle (DetailView):
    model =Alarma 
class  AlarmaActualizar(SuccessMessageMixin,UpdateView):
    model =  Alarma
    form = Alarma
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Alarma Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leera') # Redireccionamos a la vista principal 'leer'
class AlarmaEliminar(SuccessMessageMixin, DeleteView): 
    model = Alarma 
    form = Alarma
    fields = "__all__"    
# Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Alarma Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leera') # Redireccionamos a la vista principal 'leer'
#-----------------------------ALARMA----------------------------------------------------#  
# 
# #-----------------------------HISTORIAL----------------------------------------------------#  
class ListadoHistorial(ListView):
    model =Historial
class HistorialCrear(SuccessMessageMixin, CreateView):
    model = Historial
    form = Historial
    fields = "__all__"
    success_message ='Historial creado correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerhi') # Redireccionamos a la vista principal 'leer' 
class HistorialDetalle(DetailView):
    model =Historial 
class  HistorialActualizar(SuccessMessageMixin,UpdateView):
    model =  Historial
    form = Historial
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Historial actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerhi') # Redireccionamos a la vista principal 'leer'    
class HistorialEliminar(SuccessMessageMixin, DeleteView): 
    model = Historial
    form = Historial
    fields = "__all__"   
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Historial eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerhi') # Redireccionamos a la vista principal 'leer'
#-----------------------------HISTORIAL----------------------------------------------------#  

#-----------------------------TIPO DE ALARMA----------------------------------------------------#  
class ListadoTalarma(ListView):
    model =Talarma    
class TalarmaCrear(SuccessMessageMixin, CreateView):
    model = Talarma
    form = Talarma
    fields = "__all__"
    success_message ='Tipo de alarma creada correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerta') # Redireccionamos a la vista principal 'leer' 
class TalarmaDetalle (DetailView):
    model =Talarma 
class  TalarmaActualizar(SuccessMessageMixin,UpdateView):
    model =  Talarma
    form = Talarma
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipo de alarma actualizada correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerta') # Redireccionamos a la vista principal 'leer'    
class TalarmaEliminar(SuccessMessageMixin, DeleteView): 
    model = Talarma
    form = Talarma
    fields = "__all__"   
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipo de alarma eliminada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerta') # Redireccionamos a la vista principal 'leer'
#-----------------------------TIPO DE ALARMA----------------------------------------------------#  

#-----------------------------INVENTARIO----------------------------------------------------#  
class ListadoInventario(ListView):
    model =Inventario    
class InventarioCrear(SuccessMessageMixin, CreateView):
    model = Inventario
    form = Inventario
    fields = "__all__"
    success_message ='Inventario creado correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerin') # Redireccionamos a la vista principal 'leer' 
class InventarioDetalle (DetailView):
    model =Inventario 
class  InventarioActualizar(SuccessMessageMixin,UpdateView):
    model =  Inventario
    form = Inventario
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Inventario actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerin') # Redireccionamos a la vista principal 'leer'    
class InventarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Inventario
    form = Inventario
    fields = "__all__"   
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Inventario eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerin') # Redireccionamos a la vista principal 'leer'
#-----------------------------INVENTARIO----------------------------------------------------#  

#-----------------------------GEOLOCALIZACION----------------------------------------------------#  
class ListadoGeolocalizacion(ListView):
    model =Geolocalizacion    
class GeolocalizacionCrear(SuccessMessageMixin, CreateView):
    model = Geolocalizacion
    form = Geolocalizacion
    fields = "__all__"
    success_message ='Geolocalizacion creado correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leergeo') # Redireccionamos a la vista principal 'leer' 
class GeolocalizacionDetalle (DetailView):
    model =Geolocalizacion 
class  GeolocalizacionActualizar(SuccessMessageMixin,UpdateView):
    model =  Geolocalizacion
    form = Geolocalizacion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Geolocalizacion actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leergeo') # Redireccionamos a la vista principal 'leer'    
class GeolocalizacionEliminar(SuccessMessageMixin, DeleteView): 
    model = Geolocalizacion
    form = Geolocalizacion
    fields = "__all__"   
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Geolocalizacion eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leergeo') # Redireccionamos a la vista principal 'leer'
#-----------------------------GEOLOCALIZACION----------------------------------------------------#  

#-----------------------------TIPODOCUMENTO----------------------------------------------------#  
class ListadoTdocumento(ListView):
    model =Tdocumento    
class TdocumentoCrear(SuccessMessageMixin, CreateView):
    model = Tdocumento
    form = Tdocumento
    fields = "__all__"
    success_message ='Tipo documento creado correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leertd') # Redireccionamos a la vista principal 'leer' 
class TdocumentoDetalle (DetailView):
    model =Tdocumento 
class  TdocumentoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tdocumento
    form = Tdocumento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipo documento actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leertd') # Redireccionamos a la vista principal 'leer'    
class TdocumentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tdocumento
    form = Tdocumento
    fields = "__all__"   
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipo documento eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leertd') # Redireccionamos a la vista principal 'leer'
#-----------------------------TIPODOCUMENTO----------------------------------------------------#  

#-----------------------------EVENTO----------------------------------------------------#  
class ListadoEvento(ListView):
    model =Evento    
class EventoCrear(SuccessMessageMixin, CreateView):
    model = Evento
    form = Evento
    fields = "__all__"
    success_message ='Evento creado correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerev') # Redireccionamos a la vista principal 'leer' 
class EventoDetalle (DetailView):
    model =Evento 
class  EventoActualizar(SuccessMessageMixin,UpdateView):
    model =  Evento
    form = Evento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Evento actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerev') # Redireccionamos a la vista principal 'leer'    
class EventoEliminar(SuccessMessageMixin, DeleteView): 
    model = Evento
    form = Evento
    fields = "__all__"   
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Evento eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerev') # Redireccionamos a la vista principal 'leer'
#-----------------------------EVENTO----------------------------------------------------#  

#-----------------------------FCABEZA----------------------------------------------------#  
class ListadoFcabeza(ListView):
    model =Fcabeza    
class FcabezaCrear(SuccessMessageMixin, CreateView):
    model = Fcabeza
    form = Fcabeza
    fields = "__all__"
    success_message ='Fcabeza creado correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerfc') # Redireccionamos a la vista principal 'leer' 
class FcabezaDetalle (DetailView):
    model =Fcabeza 
class  FcabezaActualizar(SuccessMessageMixin,UpdateView):
    model =  Fcabeza
    form = Fcabeza
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Fcabeza actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerfc') # Redireccionamos a la vista principal 'leer'    
class FcabezaEliminar(SuccessMessageMixin, DeleteView): 
    model = Fcabeza
    form = Fcabeza
    fields = "__all__"   
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Fcabeza eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerfc') # Redireccionamos a la vista principal 'leer'
#-----------------------------FCABEZA----------------------------------------------------#  

#-----------------------------FCUERPO----------------------------------------------------#  
class ListadoFcuerpo(ListView):
    model =Fcuerpo    
class FcuerpoCrear(SuccessMessageMixin, CreateView):
    model = Fcuerpo
    form = Fcuerpo
    fields = "__all__"
    success_message ='Fcuerpo creado correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerfcu') # Redireccionamos a la vista principal 'leer' 
class FcuerpoDetalle (DetailView):
    model =Fcuerpo 
class  FcuerpoActualizar(SuccessMessageMixin,UpdateView):
    model =  Fcuerpo
    form = Fcuerpo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Fcuerpo actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerfcu') # Redireccionamos a la vista principal 'leer'    
class FcuerpoEliminar(SuccessMessageMixin, DeleteView): 
    model = Fcuerpo
    form = Fcuerpo
    fields = "__all__"   
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Fcuerpo eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerfcu') # Redireccionamos a la vista principal 'leer'
#-----------------------------FCUERPO----------------------------------------------------#  

#-----------------------------RELACION----------------------------------------------------#  
class ListadoRelacion(ListView):
    model =Relacion    
class RelacionCrear(SuccessMessageMixin, CreateView):
    model = Relacion
    form = Relacion
    fields = "__all__"
    success_message ='Relacion creado correctamente'     
    def get_success_url(self):        
        return reverse('modulo1:leerrel') # Redireccionamos a la vista principal 'leer' 
class RelacionDetalle (DetailView):
    model =Relacion 
class  RelacionActualizar(SuccessMessageMixin,UpdateView):
    model =  Relacion
    form = Relacion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Relacion actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre  
    def get_success_url(self):               
        return reverse('modulo1:leerrel') # Redireccionamos a la vista principal 'leer'    
class RelacionEliminar(SuccessMessageMixin, DeleteView): 
    model = Relacion
    form = Relacion
    fields = "__all__"   
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Relacion eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('modulo1:leerrel') # Redireccionamos a la vista principal 'leer'
#-----------------------------RELACION----------------------------------------------------#  
