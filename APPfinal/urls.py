from django.urls import path
from .views import *




urlpatterns = [
    path('', clientes, name='Nombre'),
    path('Tramite/', Tramite, name='Tramite'),
    path('Fecha/', Fecha, name='Inicio'),
    path('Documentacion/', Documentacion, name='Documento'),
    path('Pago/', Pago, name='Pago'),
    path('index/', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sobremi/', sobremi, name='sobremi'),
    path('buscar/', buscarView, name='buscar'),
    path('ver-cliente/<int:pk>', verClienteView, name='ver-cliente'),
]