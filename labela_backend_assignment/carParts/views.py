from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from carParts.serializer import CarPartSerializer
from carParts.models import CarPart


allowedMethods = ['GET', 'POST', 'PUT', 'DELETE']


@api_view(allowedMethods)
def carParts(request):
    result = {}
# GET
    if request.method == 'GET':
        tempObjects = CarPart.objects.all()
        serializer = CarPartSerializer(tempObjects, many=True)
        return Response({'message': 'Successfully retrieved all person data',  'data': serializer.data})
# POST
    elif request.method == 'POST':
        inpuData = request.data
        serializer = CarPartSerializer(data=inpuData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
# PUT
    elif request.method == 'PUT':
        inputData = request.data  # Collect data from user
        serializer = CarPartSerializer(data=inputData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
# PATCH
    elif request.method == 'PATCH':
        try:
            person_obj = CarPart.objects.get(id=request.data['id'])
            inputData = request.data
        except CarPart.DoesNotExist:
            return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarPartSerializer(
            person_obj, data=inputData, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"The Car part with  with ID  {request.data['id']} has been successfully updated."})
        return Response(serializer.errors)
# DELETE
    elif request.method == 'DELETE':
        try:
            person_obj = CarPart.objects.get(id=request.data['id'])
            person_obj.delete()
            return Response({"message": f"The Car part with  with ID {request.data['id']} has been successfully removed."})
        except CarPart.DoesNotExist:
            return Response({"error": "Car Part not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({"error": "Unsupported method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
