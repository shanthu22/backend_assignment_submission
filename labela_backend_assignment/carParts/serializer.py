from carParts.models import CarPart
from rest_framework import serializers

class CarPartSerializer(serializers.ModelSerializer):
    class Meta:
        model =  CarPart
        fields = ['id','part_name','description','price','quantity_available']

    # def validate(self, attrs):
    #     if(attrs['price']< 0):
    #         raise serializers.ValidationError('Price Cant be a negative Number')
    #     #elif(attrs['quantity_available']):
    #         #Alert Owner
    #     return super().validate(attrs)
