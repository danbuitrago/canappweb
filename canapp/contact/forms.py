from django import forms            #se importa la libreria formularios forms

class ContactForm(forms.Form):
    name=forms.CharField(label='Nombre', max_length=200,required=True)
    email=forms.EmailField(label='Correo',max_length=100,required=True)
    content=forms.CharField(label='Contenido', max_length=200,required=True,widget=forms.Textarea)



