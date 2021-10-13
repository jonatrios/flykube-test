from rest_framework import serializers
from .models import TravelModel

class TraverModelSerializar(serializers.ModelSerializer):
    class Meta:
        model = TravelModel
        fields = '__all__'


    def to_representation(self, instance):
        return {
            'id' : instance.id,
            'start_date' : instance.start_date,
            'end_date' :instance.end_date,
            'confirmed' : instance.confirmed,
            'destination' : instance.destination.destination_name,
            'passenger' : instance.passenger.all().values()
        }