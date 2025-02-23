from .models import Cart
from rest_framework import serializers

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','user', 'products', 'total_price']
        