from django.shortcuts import render
from .models import Service         #importamos el modelo Service

# Create your views here.

def services(request):
    services=Service.objects.all()
    return render (request,'services/services.html',{'services':services})
