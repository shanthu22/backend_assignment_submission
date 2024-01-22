from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.process.productProcess import HandleGetProcess, HandlePostProcess, HandlePutProcess, HandleDeleteProcess
from products.process.allProductProcess import HandleGetAllProcess
allowedHttpMethods = ['GET', 'POST', 'PUT', 'DELETE']


@api_view(allowedHttpMethods)
# This method fetches the productID, Http Methods and calls the appropriate function from productProcess.py
# Params:HTTP Request, *callback_args, **callback_kwargs
def HandleProductsRequest(request, *callback_args, **callback_kwargs):
    inputData = {}
    productID = callback_kwargs.get('productID', None)
    print("+++++++++++++++++++++++++++++++")
    print(f'productID: {productID}')
    print("+++++++++++++++++++++++++++++++")
    if request.method == 'GET':
        inputData['id'] = productID
        output = HandleGetProcess(inputData)
        return Response(output)

    elif request.method == 'POST':
        print('++++++++++++++++++++++')
        print('POST method')
        print('++++++++++++++++++++++')
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
    # except Exception as e:
    #     print('++++++++++++++++++++++')
    #     print('Exception handling')
    #     print(f'Exception: {str(e)}')
    #     print('++++++++++++++++++++++')
    #     return Response(
    #         {"message": f"An error occurred: {str(e)}"},
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #     )


@api_view(allowedHttpMethods)
def HandleAllProductsRequest(request, *callback_args, **callback_kwargs):
    inputData = {}
    productID = callback_kwargs.get('productID', None)
    print("+++++++++++++++++++++++++++++++")
    print(f'productID: {productID}')
    print("+++++++++++++++++++++++++++++++")
    if request.method == 'GET':
        # inputData = request.data
        output = HandleGetAllProcess(inputData)
        return Response(output)
