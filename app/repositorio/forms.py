from django import forms

from repositorio.models import Document

#formulario para la creacion de un nuevo registro 
class DocumentCreateForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['user','title']
        
        widgets = {
            "title": forms.TextInput(attrs={
                'class':'form-control ',
            })
        }
