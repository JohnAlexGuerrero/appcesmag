from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from cuenta.forms import RegisterUserForm

from cuenta.models import CustomUser, Profile

from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import DetailView

# Create your views here.
class UserLoginView(TemplateView):
    template_name = "autenticacion/login.html"
    
    def post(self, request):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(email=email, password=password)
        
        if user:
            login(request, user)
            if user.is_authenticated:
                # if user.academica.rol == "":
                #messages.success(request, 'Necesitas crear un perfil.')
                #     return redirect('role')
                # else:
                #     messages.success(request, 'You have been logged in.')
                return redirect('home')
        else:
            messages.success(request, 'There was Error logging in, Please try again.')
            return redirect('login')

#view register
class CustomUserCreateView(TemplateView):
    model = CustomUser
    template_name = "autenticacion/signup.html"
    
    def post(self, request):
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
              form.save()
              #Authentication and login
              email = form.cleaned_data['email']
              password = form.cleaned_data['password1']
              user = authenticate(email=email, password=password)
              login(request, user)
              messages.success(request, 'You have successfull.')

              if user.is_authenticated:
                # return redirect("profile_new", slug=user.profile.slug)
                return redirect('login')
        else:
            form = RegisterUserForm()
        return redirect('signup')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegisterUserForm
        # context["app"] = App.objects.first()
        return context

#perfil create
class UserProfileView(LoginRequiredMixin ,UpdateView):
    model = Profile
    template_name = "autenticacion/perfil_edit.html"
    fields = '__all__'
    success_url = reverse_lazy('perfil')
    
#detail perfil
class ProfileDetailView(DetailView):
    model = Profile
    template_name = "autenticacion/perfil_detail.html"