from rest_framework import serializers, permissions
from .models import Gym, Trainer, Client, WorkoutSession

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Gym
        fields = ['Name','Address','url']

class TrainerSerializer(serializers.ModelSerializer):
    #Gym = serializers.CharField(source='Gym.Name')
    class Meta:
        model = Trainer
        fields = ['Name','Specialization','Gym','url']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['Name','Age','url']

class WorkoutSessionSerializer(serializers.ModelSerializer):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    class Meta:
        model = WorkoutSession
        fields = ['Client','Trainer','Date', 'Duration','url']