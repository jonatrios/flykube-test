from django.http import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers import TraverModelSerializar

class TravelGenericViewSet(GenericViewSet):


    serializer_class = TraverModelSerializar
        
    def __init__(self, **kwargs) -> None:
        self.name = 'Travel Api List'
        self.description = 'List all travels registred in data base'


    def get_queryset(self, pk=None):
        if pk is None: 
            return self.get_serializer().Meta.model.objects.filter(confirmed=True)
        return self.get_serializer().Meta.model.objects.filter(confirmed=True, id=pk).first()

    def list(self, request):
        product_list = self.get_serializer(self.get_queryset(), many=True)
        return Response(product_list.data, status=status.HTTP_200_OK)


    def create(self, request):
        pass