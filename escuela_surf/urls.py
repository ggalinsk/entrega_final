from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import ClaseListView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.vista_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_alumno, name='registro_alumno'),
    path('perfil/', views.perfil_alumno, name='perfil_alumno'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('clases/', ClaseListView.as_view(), name='clase_list'),
]
