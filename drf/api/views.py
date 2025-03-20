from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TagSerializer
from recipes.models import Tag

# Представления с использованием класса APIView (низкоуровневые) - простейшие примеры

# Получение списка тегов и добавление тега
class TagListCreateApiView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagRetriveUpdateDeleteApiView(APIView):
    def get(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        ...
