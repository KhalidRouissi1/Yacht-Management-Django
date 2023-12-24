from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from yachtStore.models import Yacht
from .serializers import YachtSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(method='get', manual_parameters=[
    openapi.Parameter('param_name', openapi.IN_QUERY, description="Description of the query parameter", type=openapi.TYPE_STRING),
])
@api_view(['GET'])
def getData(request):
    serializer = YachtSerializer(Yacht.objects.all(), many=True)
    return Response(serializer.data)
@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'yid': openapi.Schema(type=openapi.TYPE_STRING),
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'price': openapi.Schema(type=openapi.TYPE_STRING),
            'yachtPhoto': openapi.Schema(type=openapi.TYPE_STRING, format='binary'),  
        },
        required=['yachtPhoto', 'price', 'description', 'title', 'yid']  
    )
)
@api_view(['POST'])
def addItem(request):
    serializer = YachtSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=openapi.Schema(type=openapi.TYPE_OBJECT))
@api_view(['PUT'])
def editItem(request, pk):
    try:
        item = Yacht.objects.get(pk=pk)
    except Yacht.DoesNotExist:
        return Response({'message': 'Yacht not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = YachtSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete')
@api_view(['DELETE'])
def deleteItem(request, pk):
    try:
        item = Yacht.objects.get(pk=pk)
    except Yacht.DoesNotExist:
        return Response({'message': 'Yacht not found'}, status=status.HTTP_404_NOT_FOUND)

    item.delete()
    return Response({'message': 'Yacht deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
