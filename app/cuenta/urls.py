from django.urls import path

from cuenta.views import UserLoginView, CustomUserCreateView, UserProfileView,ProfileDetailView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registro/', CustomUserCreateView.as_view(), name='signup'),
    path('perfil/<slug:slug>/edit/', UserProfileView.as_view(), name='perfil-edit'),
    path('perfil/<slug:slug>/', ProfileDetailView.as_view(), name='perfil'),
]
