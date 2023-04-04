from django.urls import path        #se importa path desde django urls
from . import views

urlpatterns=[
    path('', views.services ,name='services'),
]