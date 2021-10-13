from rest_framework import serializers
from .models import TravelModel

class TraverModelSerializar(serializers.ModelSerializer):
    class Meta:
        model = TravelModel
        fields = '__all__'