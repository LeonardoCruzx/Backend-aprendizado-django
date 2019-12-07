from django.urls import path

from .views import *

urlpatterns = [
    path('pessoas',lista_pessoas),
]

