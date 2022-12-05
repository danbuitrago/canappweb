from django.shortcuts import render

def Home(request):
    return render (request, "index.html")

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

# Create your views here.
#-----------------------------Mascotas----------------------------------------------------#
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
 
 #-----------------------------Mascotas----------------------------------------------------#  
 
  #-----------------------------Persona----------------------------------------------------# 
   
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
 
 #-----------------------------Persona----------------------------------------------------#  

 
#-----------------------------VISTAS DE EMPRESA--------------------------------------------#     
 #-----------------------------Empresa-----------------------------------------------------#     

class ListadoEmpresa(ListView):
    model = Empresa
    
class EmpresaCrear(SuccessMessageMixin, CreateView):
    model = Empresa
    form = Empresa
    fields = "__all__"
    success_message ='Mascota creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
class EmpresaDetalle (DetailView):
    model =Empresa
 
class  EmpresaActualizar(SuccessMessageMixin,UpdateView):
    model =  Empresa
    form = Empresa
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Mascota Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class EmpresaEliminar(SuccessMessageMixin, DeleteView): 
    model = Empresa
    form = Empresa
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Mascota Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
#-----------------------------Empresa-----------------------------------------------------#  
#----------------------------VISTAS DE EMPRESA--------------------------------------------#      





#-----------------------------Tipo animal----------------------------------------------------# 
class ListadoTanimal(ListView):
    model = Tanimal
    
class TanimalCrear(SuccessMessageMixin, CreateView):
    model = Tanimal
    form = Tanimal
    fields = "__all__"
    success_message ='Tipo animal creado correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
class tanimalDetalle (DetailView):
    model =Tanimal
 
class  TanimalActualizar(SuccessMessageMixin,UpdateView):
    model =  Tanimal
    form = Tanimal
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipo animal actualizado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class TanimalEliminar(SuccessMessageMixin, DeleteView): 
    model = Tanimal
    form = Tanimal
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipo animal eliminado correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
#-----------------------------Tipo animal----------------------------------------------------#  





#-----------------------------Raza----------------------------------------------------# 
class Listadoraza(ListView):
    model =Raza
    
class RazaCrear(SuccessMessageMixin, CreateView):
    model = Raza
    form = Raza
    fields = "__all__"
    success_message ='Raza creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
class RazaDetalle (DetailView):
    model =Raza
 
class  RazaActualizar(SuccessMessageMixin,UpdateView):
    model =  Raza
    form = Raza
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Raza actualizada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class RazaEliminar(SuccessMessageMixin, DeleteView): 
    model = Raza
    form = Raza
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Raza eliminada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

#-----------------------------Raza----------------------------------------------------#  



#-----------------------------Especie----------------------------------------------------#  
class ListadoEspecie(ListView):
    model =Especie
    
class EspecieCrear(SuccessMessageMixin, CreateView):
    model = Especie
    form = Especie
    fields = "__all__"
    success_message ='Especie creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
class EspecieDetalle (DetailView):
    model =Especie
 
class  EspecieActualizar(SuccessMessageMixin,UpdateView):
    model =  Especie
    form = Especie
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Especie actualizada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class EspecieEliminar(SuccessMessageMixin, DeleteView): 
    model = Especie
    form = Especie
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Especie eliminada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

#-----------------------------Especie----------------------------------------------------#  



#-----------------------------Tipo persona----------------------------------------------------#  
class ListadoTpersona(ListView):
    model =Tpersona
    
    
class TpersonaCrear(SuccessMessageMixin, CreateView):
    model = Tpersona
    form = Tpersona
    fields = "__all__"
    success_message ='Tipo persona creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
class TpersonaDetalle (DetailView):
    model =Tpersona
 
class TpersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tpersona
    form = Tpersona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipo persona actualizada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class TpersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tpersona
    form = Tpersona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipo persona eliminada correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

#-----------------------------Tipo persona---------------------------------------------------#  


#-----------------------------Tipo Documento ----------------------------------------------------#  
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

#-----------------------------Tipo Documento ---------------------------------------------------#  

