
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import *


#PRODUTOS
@api_view(['GET','PUT'])
@permission_classes((AllowAny,))
def lista_de_produtos(request):

    if request.method == 'GET':
        produtos = ProdutoModel.objects.all()
        serializer = ProdutoSerializer(produtos,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalhes_de_produtos(request,pk):

    try:
        produto = ProdutoModel.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#CATEGORIAS
@api_view(['GET','PUT'])
@permission_classes((AllowAny,))
def lista_de_categorias(request):

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
def detalhes_de_categorias(request,pk):

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


