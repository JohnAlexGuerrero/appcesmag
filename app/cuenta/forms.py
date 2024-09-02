from django import forms
from django.contrib.auth.forms import UserCreationForm

from cuenta.models import CustomUser

#formulario para el registro de un nuevo usuario
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control ', 'placeholder':'Correo electrónico'})
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de usuario','type':'text'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','placeholder':'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','placeholder':'Confirmación de password'})
    )
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Enter your name'})
    )
    second_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Enter your second name'})
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Enter your last_name'})
    )
    second_last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Enter your last_name'})
    )
    
    class Meta:
        model = CustomUser
        fields = ['email','username','password1','password2','first_name','second_name','last_name','second_last_name']
