from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from shoppingCarts.models import ShoppingCart
from shoppingCarts.process.shoppingCartProcess import handleGETMethod, handlePostMethod, handleDeleteMethod
from rest_framework.pagination import PageNumberPagination
allowedMethods = ['GET', 'POST', 'PUT', 'DELETE']


@api_view(allowedMethods)
def shoppingCart(request, RequestedUserID):
    pagination_class = PageNumberPagination

    # GET Method
    if request.method == 'GET':
        try:
            handleGETMethod(RequestedUserID)
            return Response({"message": handleGETMethod(RequestedUserID)})

        except ShoppingCart.DoesNotExist:
            return Response({"message": "ShoppingCart not found for the specified user"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# POST Method
    elif request.method == 'POST':

        inputData = {"UserID": RequestedUserID}  # Adding UserID
        inputData.update(request.data)  # Adding the CarPartID

        try:
            return Response({"message": handlePostMethod(inputData)})

        except ShoppingCart.DoesNotExist:
            return Response({"message": "ShoppingCart not found for the specified user ID"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# DELETE Method
    elif request.method == 'DELETE':

        inputData = {"UserID": RequestedUserID}  # Adding UserID
        inputData.update(request.data)  # Adding the CarPartID

        try:
            return Response({"message": handleDeleteMethod(inputData)})

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({"error": "Unsupported method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
