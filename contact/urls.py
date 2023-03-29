from django.contrib import admin
from django.urls import path, include # se importa include
#from modulo1.views import*   
from . import views

urlpatterns=[
    path('',views.contact, name='contact'),
]