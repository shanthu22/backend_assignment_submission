# File contains functions which handle all the HTTP methods for Products from products\views.py
# HandleGetProcess
# HandlePostProcess
# HandlePutProcess
# HandleDeleteProcess
from products.models import Product
from products.serializer import ProductsSerializer
from rest_framework import status


def HandleGetAllProcess(data):
    fetchedData = Product.objects.all()
    serializer = ProductsSerializer(fetchedData, many=True)

    if not fetchedData.exists():
        return ({'message': 'Products not found'}, status.HTTP_404_NOT_FOUND)

    return ({'message': 'Successfully retrieved all person data',  'data': serializer.data}, status.HTTP_200_OK)


def HandlePostAllProcess():
    return 'HandlePostProcess called'


def HandlePutAllProcess():
    return 'HandlePutProcess called'


def HandleDeleteAllProcess():
    return 'HandleDeleteProcess called'
