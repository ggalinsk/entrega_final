from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.vista_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_alumno, name='registro_alumno'),
    path('perfil/', views.perfil_alumno, name='perfil_alumno'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
]
