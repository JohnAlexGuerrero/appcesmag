from django.urls import path

from home.views import HomeView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
]
