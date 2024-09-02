from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.db.models import Q

from django.shortcuts import render
from django.urls import reverse_lazy


from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from repositorio.models import Repositorio, Document, Categoria, Image

# from repositorio.forms import DocumentCreateForm

# Create your views here.
class RepositorioCreateView(CreateView):
    model = Repositorio
    template_name = "repositorio/new.html"
    fields = ['titulo','user']
       
    def get_success_url(self):
        return reverse_lazy('repositorio_detail', kwargs={'pk': self.object.id})

class RepositorioDetailView(DetailView):
    model = Repositorio
    template_name = "repositorio/detail.html"
    
    def get_queryset(self):
        return super().get_queryset()
    
    def get_logo(self):
      return Image.objects.filter(repositorio__id=self.kwargs['pk']).filter(name__icontains='logo').first()
    
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["categoria_documents"] = Categoria.choices
      context['logo'] = self.get_logo
      return context
  


# class DocumentListView(ListView):
#     model = Document
#     template_name = "repositorio/list_document.html"

#view utilizado para la creacion de un nuevo registro
class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = Document
    template_name = "repositorio/new.html"
    form_class = '__all__'
    
    # def get_success_url(self):
    #     print(self.object)
    #     return reverse_lazy('logo', kwargs={'slug': self.object.slug })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = '__all__' #DocumentCreateForm
        # context["app"] = App.objects.first()
#         return context

#images upload
class LogoView(CreateView):
  model = Image
  fields = '__all__'
  success_url = reverse_lazy('home')
  template_name = "repositorio/logo.html"
  
  def get_object(self, *args, **kwargs):
    return Repositorio.objects.get(id=self.kwargs['pk'])
  
  def get_logo_obj(self, *args, **kwargs):
    logo = Image.objects.filter(repositorio__id=self.kwargs['pk']).filter(name__icontains='logo').first()
  
    if logo:
      return logo
    return ''
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["object"] = self.get_object
    context["logo"] = self.get_logo_obj
    return context
  
#view para actualizar el logo del software
class ImageUpdateView(UpdateView):
  model = Image
  fields = ("id","thumbnail","name",)
  template_name = "repositorio/logo.html"
  
  def get_object(self, *args, **kwargs):
    return Image.objects.get(id=self.kwargs['pk'])
  
  def get_success_url(self):
    super().get_success_url()
    return reverse_lazy('repositorio_detail', kwargs={'pk':self.get_object().repositorio.id})
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context
  
    
class DocumentView(TemplateView):
    template_name = "repositorio/document.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["manual_tecnico"] = {
            "titulo": "Manual Técnico del Sistema XYZ",
  "version": "1.0",
  "fecha": "2023-10-27",
  "autores": ["Juan Pérez", "María García"],
  "secciones": {
    "introduccion": {
      "descripcion": "Descripción general del sistema.",
      "paginas": [1, 2, 3]
    },
    "arquitectura": {
      "descripcion": "Diagramas y explicación de la arquitectura del sistema.",
      "paginas": [4, 5, 6, 7]
    },
    "componentes": {
      "descripcion": "Descripción detallada de cada componente del sistema.",
      "paginas": [8, 9, 10, 11, 12]
    },
    "api": {
      "descripcion": "Documentación de la interfaz de programación de aplicaciones (API).",
      "paginas": [13, 14, 15, 16]
    },
    "instalacion": {
      "descripcion": "Pasos para instalar y configurar el sistema.",
      "paginas": [17, 18, 19]
    },
    "mantenimiento": {
      "descripcion": "Procedimientos para el mantenimiento del sistema.",
      "paginas": [20, 21]
    },
    "solucion_problemas": {
      "descripcion": "Guía para solucionar problemas comunes.",
      "paginas": [22, 23, 24]
    }
  }
        }
        return context
    




