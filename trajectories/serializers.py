from rest_framework.serializers import ModelSerializer
from trajectories.models import Trajectories

class TrajectoriesSerializer(ModelSerializer):
    class Meta:
        model = Trajectories
        fields = ['id', 'taxi_id', 'date', 'latitude', 'longitude']