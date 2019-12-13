from django.urls import path

from .views import *

urlpatterns = [
    path('lista-de-produtos',lista_de_produtos,name="lista-de-produtos"),
    path('detalhes-de-produtos/<int:pk>',detalhes_de_produtos,name="detalhes-de-produtos"),
    path('lista-de-categorias',lista_de_categorias,name="lista-de-categorias"),
    path('detalhes-de-categorias/<int:pk>',detalhes_de_categorias,name="detalhes-de-categorias")
]

