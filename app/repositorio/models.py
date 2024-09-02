from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from io import BytesIO
from PIL import Image
from django.core.files import File

from cuenta.models import CustomUser

# Create your models here.
class Repositorio(models.Model):
    titulo = models.CharField(max_length=50, null=False, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = ("Repositorio")
        verbose_name_plural = ("Repositorios")

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("repositorio_detail", kwargs={"pk": self.pk})
    
    def get_logo(self):
        return Image.objects.filter(repositorio_id=self.id).filter(name__icontains='logo').first()

class Categoria(models.TextChoices):
    # Documentos Técnicos
    MANUAL_TECNICO = 'Manual-Tecnico', 'Manual Técnico'
    MANUAL_USUARIO = 'Manual-de-Usuario', 'Manual de Usuario'
    # ESPECIFICACION_TECNICA = 'ET', 'Especificación Técnica'
    DOCUMENTACION_API = 'Documentacion-API', 'Documentación de API'
    GUIA_INSTALACION = 'Guia-de-Instalacion', 'Guía de Instalación'
    # INFORME_TECNICO = 'IT', 'Informe Técnico'
    DOCUMENTACION_CODIGO = 'Documentacion-de-Codigo', 'Documentación de Código'

class Plantilla(models.Model):
    titulo = models.CharField(max_length=150, unique=True)
    categoria = models.CharField(max_length=50, choices=Categoria.choices)
    slug = models.SlugField()
    url = models.FileField(upload_to='plantillas/', max_length=100, blank=False)
    

    class Meta:
        verbose_name = ("Plantilla")
        verbose_name_plural = ("Plantillas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Plantilla_detail", kwargs={"pk": self.pk})

    
class Document(models.Model):    
    title = models.CharField(max_length=150, null=False)
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=50, null=False)
    slug = models.SlugField()
    user = models.ForeignKey(CustomUser, verbose_name=("user"), on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50, choices=Categoria.choices, null=True)
    logo = models.ImageField(upload_to='uploads', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Documento")
        verbose_name_plural = ("Documentos")

    def __str__(self):
        return self.title
    
    # def get_authors(self):
    #     return Author.objects.filter(software__slug=self.slug)

    # def get_absolute_url(self):
    #     return reverse("Software_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    # def get_requeriments(self):
    #     return Requeriment.objects.all().filter(software_id=self.id)
    
    def get_logo(self):
        if self.logo:
            return 'http://127.0.0.1:8000' + self.logo.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.logo:
                self.thumbnail = self.make_thumbnail(self.logo)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class Image(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True, unique=True)
    thumbnail = models.ImageField(upload_to="images/",blank=True, null=True)
    repositorio = models.ForeignKey(Repositorio, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = ("Image")
        verbose_name_plural = ("Images")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # if self.slug is None:
        #     self.slug = slugify(self.name)
        #     self.save()
            
        return f'http://127.0.0.1:8000/images/{self.id}'
    
    def get_image(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        
        return ''

#model: caracteristicas