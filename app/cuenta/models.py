from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    second_last_name = models.CharField(max_length=50, blank=True, null=True)
    
    #campo identificador unico del User
    USERNAME_FIELD = 'email'
    
    #forzar a introducir un campo
    REQUIRED_FIELDS = ['username','password']
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    class Gender(models.TextChoices):
        HOMBRE = 'Hombre'
        MUJER = 'Mujer'
    
    class Ocupacion(models.TextChoices):
        PROFESIONAL = 'Profesional'
        ESTUDIANTE = 'Estudiante'
        DESARROLLADO = 'Desarrollador'
        
    user = models.OneToOneField(CustomUser, verbose_name=("user"), on_delete=models.CASCADE)
    gender = models.SmallIntegerField(choices=Gender.choices, blank=True, null=True)
    phone = models.CharField(("número de contacto"), max_length=50, blank=True, null=True)
    ocupacion = models.CharField(max_length=150, choices=Ocupacion.choices, blank=True, null=True)
    academia = models.CharField(max_length=150, blank=True, null=True)
    slug = models.SlugField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)
