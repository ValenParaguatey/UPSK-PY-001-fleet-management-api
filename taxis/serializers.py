from rest_framework.serializers import ModelSerializer
from taxis.models import Taxi

class TaxiSerializer(ModelSerializer):
    class Meta:
        model = Taxi
        fields = ['id', 'plate']
        
