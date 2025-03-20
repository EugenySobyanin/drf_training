from django.urls import path

from .views import TagListCreateApiView, TagRetriveUpdateDeleteApiView


urlpatterns = [
    path('tags/', TagListCreateApiView.as_view()),
    path('tags/<int:pk>/', TagRetriveUpdateDeleteApiView.as_view()),
]
