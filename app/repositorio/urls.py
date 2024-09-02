from django.urls import path

from repositorio.views import DocumentCreateView, DocumentView#, DocumentListView, ScreenShortCreateView 
from repositorio.views import RepositorioCreateView, RepositorioDetailView, LogoView, ImageUpdateView

urlpatterns = [
    path('new/', RepositorioCreateView.as_view(), name='repositorio_new'),
    path('<int:pk>/', RepositorioDetailView.as_view(), name='repositorio_detail'),
    
    # path('', DocumentListView.as_view(), name='documents'),
    path('doc/new/',DocumentCreateView.as_view(), name='documento_new'),
    path('doc/<str:link>/', DocumentView.as_view(), name='document'),
    # path('write/',DocumentView.as_view(), name='document_write'),
    
    # path('<int:pk>/image/upload/', ImageCreateView.as_view(), name='upload'),
    path('<int:pk>/logo/upload/', LogoView.as_view(), name='logo_upload'),
    path('<int:pk>/image/update/', ImageUpdateView.as_view(), name='image_update'),
]
