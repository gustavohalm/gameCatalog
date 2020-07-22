from rest_framework import viewsets
from .serializers import CategorySerializer, PublisherSerializer, GameSerializer
from .models import Category, Publisher, Game


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    filterset_fields = ('category', 'publisher', 'name')
