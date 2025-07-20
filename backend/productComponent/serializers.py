from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.modelSerializer):
    class Meta:
        model = Product
        fields = ['productId', 'title', 'price', 'quantity']
        extra_kwags = {'productId': {'read_only': True}}