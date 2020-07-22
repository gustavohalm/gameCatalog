from rest_framework import serializers
from .models import Category, Publisher, Game


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id',)


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
        read_only_fields = ('id',)


class GameSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=Category.objects.all(), write_only=True)

    publisher = PublisherSerializer(read_only=True)
    publisher_id = serializers.PrimaryKeyRelatedField(source='publisher', queryset=Publisher.objects.all(), write_only=True)

    class Meta:
        model = Game
        fields = ('id', 'name', 'description', 'publication_year', 'price', 'category', 'category_id', 'publisher', 'publisher_id')
        read_only_fields = ('id',)
