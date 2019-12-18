from django.urls import path

from .views import *

urlpatterns = [
    path('lista-de-usuarios',lista_de_usarios),
    path('detalhes-de-usuarios',detalhes_de_usuarios),
    path('login',login)
]

