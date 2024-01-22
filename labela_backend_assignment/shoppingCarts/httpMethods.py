from users.models import User
from carParts.models import CarPart
from shoppingCarts.serializer import ShoppingCartsSerializer
from shoppingCarts.models import ShoppingCart
from django.shortcuts import get_object_or_404


def handleGETMethod(data):
    shopping_cart = ShoppingCart.objects.filter(UserID=data)
    if not shopping_cart.exists():
        raise ShoppingCart.DoesNotExist
        return 'ShoppingCart not found for the specified user'
    serializer = ShoppingCartsSerializer(shopping_cart, many=True)
    return serializer.data


def handlePostMethod(data):
    serializer = ShoppingCartsSerializer(data=data)

# Check if the User Exist
    # a=User.objects.get(pk = data['UserID'])
    # if not User.objects.get(pk = data['UserID']):
    #     #raise User.DoesNotExist
    #     return(f'User  {a}in query dfd does not exist. ')
    # if CarPart.objects.get(pk = data['CarPartID'] ):
    #     #raise CarPart.DoesNotExist
    #     return('Car part in query does not exist.')

    if not serializer.is_valid():
        return ('Either the UserID or the Product does not exist. ')

    serializer.save()
    return data


def handleDeleteMethod(data):

    shoppingCart = get_object_or_404(
        ShoppingCart, id=data['id'], UserID=data['UserID'])

    shoppingCart.delete()

    return f"The Car part with  with ID {data['id']} has been successfully removed."
