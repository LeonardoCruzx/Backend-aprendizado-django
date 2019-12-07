from django.urls import path

from .views import *

urlpatterns = [
    path('lista-de-doces',lista_doces,name="lista-de-doces"),
    path('detalhes-de-doces/<int:pk>',detalhes_doces,name="detalhes-de-doces"),
    path('lista-de-categorias',lista_categorias,name="lista-de-categorias"),
    path('detalhes-de-categorias/<int:pk>',detalhes_categorias,name="detalhes-de-categorias")
]

