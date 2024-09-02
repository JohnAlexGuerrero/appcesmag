from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from repositorio.models import Repositorio


# Create your views here.
class IndexView(TemplateView):
    template_name = "home/index.html"


class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["repositorios"] = Repositorio.objects.all()
        print(context)
        return context
    
