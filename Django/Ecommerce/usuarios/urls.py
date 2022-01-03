from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.usuarios, name='index'),
    path('login/', views.login, name='usuariosLog'),
    path('register/', views.registro, name='usuariosReg'),
]
