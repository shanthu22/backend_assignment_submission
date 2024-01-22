from products.models import Product
from shoppingCarts.models import ShoppingCart
from rest_framework import serializers


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity']
