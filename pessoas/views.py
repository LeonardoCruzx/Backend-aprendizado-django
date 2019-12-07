
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

# Create your views here.
from .models import *
from .serializers import *

@api_view(['GET','POST'])
def lista_pessoas(request):

    if request.method == 'GET':
        pessoas = PessoaModel.objects.all()
        serializer = PessoaSerializer(pessoas,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)