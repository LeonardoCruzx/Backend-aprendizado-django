
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

#DOCES
@api_view(['GET','PUT'])
def lista_doces(request):

    if request.method == 'GET':
        doces = DoceModel.objects.all()
        serializer = DocesSerializer(doces,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DocesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalhes_doces(request,pk):
    try:
        doce = DoceModel.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DocesSerializer(doce)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DocesSerializer(doce, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        doce.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#CATEGORIAS
@api_view(['GET','PUT'])
def lista_categorias(request):

    if request.method == 'GET':
        categorias = CategoriaModel.objects.all()
        serializer = CategoriaSerializer(categorias,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalhes_categorias(request,pk):
    try:
        categoria = CategoriaModel.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)