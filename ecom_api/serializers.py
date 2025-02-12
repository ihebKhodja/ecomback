from .models import Product, Category
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'created_at', 'updated_at']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Category
        fields=['id', 'name', 'products', 'created_at', 'updated_at']
