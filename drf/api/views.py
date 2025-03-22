from django.shortcuts import  get_object_or_404, render
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


# Получение одного тега, изменение, удаление
class TagRetriveUpdateDeleteApiView(APIView):

    def get_obj(self, pk):
        return get_object_or_404(Tag, pk=pk)

    def get(self, request, pk):
        tag = self.get_obj(pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        tag = self.get_obj(pk)
        serializer = TagSerializer(data=request.data, instance=tag)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        tag = self.get_obj(pk)
        serializer = TagSerializer(
            data=request.data, instance=tag, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        tag = self.get_obj(pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


