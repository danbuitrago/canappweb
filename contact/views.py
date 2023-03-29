from django.shortcuts import render, redirect           #redirect para redireccionar páginas
from .forms import ContactForm
from django.urls import reverse                     #reverse similar a template tag url
from django.core.mail import EmailMessage               #para crear la estructura de un mensaje y para enviarlo


#reate your views here.
def contact(request):
    contact_form=ContactForm()
    #si el requerimiento es POST se hace una comprobación y se recuperan los datos
    if request.method=='POST':
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            #enviamos correo y redireccionar
            email=EmailMessage(
                "Can&app: Nuevo mensaje",                                           #asunto
                "De {} <{}>\n\n Escribió: \n\n{}".format(name,email,content),       #cuerpo
                "no-contestar@inbox.mailtrap.io",                                   #origen
                ["danbuitrago1@hotmail.com"],                                       #destino
                reply_to=[email]                                                    #email de la persona de contacto
            )
            try:
                email.send()                                                            #enviar mail si todo bien
                return redirect(reverse('contact')+"?ok")  
            except:
                return redirect(reverse('contact')+"?fail")                         #enviar mail si no va bien   

    return render(request, 'contact/contact.html',{'form':contact_form})
 