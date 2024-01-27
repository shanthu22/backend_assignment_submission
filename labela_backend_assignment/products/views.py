from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.process.productProcess import HandleGetProcess, HandlePostProcess, HandlePutProcess, HandleDeleteProcess
from products.process.allProductProcess import HandleGetAllProcess, HandlePostAllProcess, HandlePutAllProcess, HandleDeleteAllProcess
from rest_framework.pagination import PageNumberPagination
allowedHttpMethods = ['GET', 'POST', 'PUT', 'DELETE']

# This class defines the pagination settings


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3  # Set the desired page size
    page_size_query_param = 'page_size'
    max_page_size = 10


@api_view(allowedHttpMethods)
# This method fetches the productID, Http Methods and calls the appropriate function from productProcess.py
# Params:HTTP Request, *callback_args, **callback_kwargs
def HandleProductsRequest(request, *callback_args, **callback_kwargs):
    inputData = {}
    productID = callback_kwargs.get('productID', None)

    if request.method == 'GET':
        inputData['id'] = productID
        output = HandleGetProcess(inputData)
        # page = self.pagination_class()
        return Response(output)

    elif request.method == 'POST':

        inputData = request.data
        output = HandlePostProcess(inputData)
        return Response(output)
    elif request.method == 'PUT':
        inputData = request.data
        output = HandlePutProcess(inputData)
        return Response(output)
    elif request.method == 'DELETE':
        inputData = request.data
        output = HandleDeleteProcess(inputData)
        return Response(output)

    return Response(
        {"message": "Unsupported method"},
        status=status.HTTP_405_METHOD_NOT_ALLOWED,
    )


@api_view(allowedHttpMethods)
# This method fetches the products data as a whole, Http Methods and calls the appropriate function from allProductProcess.py
# Params:HTTP Request, *callback_args, **callback_kwargs
def HandleAllProductsRequest(request, *callback_args, **callback_kwargs):
    inputData = {}
    productID = callback_kwargs.get('productID')
    if productID is not None:
        return Response(
            {"message": "Unsupported method/End Point.  To work with a specific product use this end point: product/Product ID here/"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    if request.method == 'GET':
        output = HandleGetAllProcess(inputData)['data']
        # Using pagination class to paginate the data
        paginator = CustomPageNumberPagination()

        result_page = paginator.paginate_queryset(output, request)

        return paginator.get_paginated_response(result_page)

        # return Response(output)

    elif request.method == 'POST':
        inputData = request.data
        output = HandlePostAllProcess(inputData)
        return Response(output)

    elif request.method == 'PUT':
        inputData = request.data
        output = HandlePostProcess(inputData)
        return Response(output)

    elif request.method == 'DELETE':
        inputData = request.data
        output = HandleDeleteAllProcess(inputData)
        return Response(output)

    return Response(
        {"message": "Unsupported method"},
        status=status.HTTP_405_METHOD_NOT_ALLOWED,
    )
