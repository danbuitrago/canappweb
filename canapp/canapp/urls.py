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
from turtle import home
from django.contrib import admin
from django.urls import path, include # se importa include
from modulo1.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings            #se importa settings para la configuracion de archivos static/media
from modulo1 import views                   #se importa views de la app modulo1
from services import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('modulo1/', include(('modulo1.urls', 'modulo1'))), # se crea una ruta modulo1 donde están todas las urls
    #llamada a los path de las static
    path('home/', Home, name='home'),
    path('home/Nosotros/', Nosotros, name='Nosotros'),
    path('home/Empresa/', Empresa, name='Empresa'),
    path('home/Ubicacion/', Ubicacion, name='Ubicacion'),
    #paths de login y logout
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),   
    #paths de app contact
    path('home/contact/', include('contact.urls')),
    #path de services
    path('home/services/',include('services.urls')),
]
#SI TENEMOS EL DEBUG EN MARCHA ACTIVAMOS LA OPCION DE SERVIR FICHEROS MEDIA EN LA STATIC_URL QUE SE BUSCAN EL EL DIRECTORIO MEDIA_ROOT
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


