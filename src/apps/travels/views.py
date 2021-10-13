from rest_framework.viewsets import GenericViewSet
from .serializers import TraverModelSerializar

class TravelGenericViewSet(GenericViewSet):


    serializer_class = TraverModelSerializar
        
    def __init__(self, **kwargs) -> None:
        self.name = 'Travel Api List'
        self.description = 'List all travels registred in data base'