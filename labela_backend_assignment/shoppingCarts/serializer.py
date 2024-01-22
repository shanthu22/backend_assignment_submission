from carParts.models import CarPart
from shoppingCarts.models import ShoppingCart
from rest_framework import serializers

class ShoppingCartsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ShoppingCart
        fields = ['id','UserID','CarPartID']

