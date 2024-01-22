# File contains functions which handle all the HTTP methods for Products from products\views.py
# HandleGetProcess
# HandlePostProcess
# HandlePutProcess
# HandleDeleteProcess
from products.models import Product
from products.serializer import ProductsSerializer
from rest_framework import status


def HandleGetProcess(inputData):

    fetched_data = Product.objects.filter(id=inputData['id'])
    serializer = ProductsSerializer(fetched_data, many=True)
    if not fetched_data.exists():
        return ({'message': 'Product not found'}, status.HTTP_404_NOT_FOUND)

    return ({'message': 'Successfully retrieved all product data',  'data': serializer.data}, status.HTTP_200_OK)


def HandlePostProcess(inputData):
    serializer = ProductsSerializer(data=inputData)
    if not serializer.is_valid():
        raise Exception(serializer.errors)

    serializer.save()
    return ({'message': 'Successfully added the product data',  'data': inputData}, status.HTTP_200_OK)


def HandlePutProcess():
    return 'HandlePutProcess called'


def HandleDeleteProcess(inputData):
    fetched_data = Product.objects.filter(id=inputData['id'])
    if not fetched_data.exists():
        return ({'message': 'Product not found'}, status.HTTP_404_NOT_FOUND)
    fetched_data.delete()

    return ({'message': f'Successfully deleted the product of id {inputData['id']}',  'data': inputData}, status.HTTP_200_OK)
