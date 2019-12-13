from django.urls import path

from .views import *

urlpatterns = [
    path('lista_de_usuarios',lista_de_usarios),
    path('detalhes_de_usuarios',detalhes_de_usuarios),
    path('login',login)
]

