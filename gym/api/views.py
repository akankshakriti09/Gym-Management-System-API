from api.serializers import GymSerializer, TrainerSerializer, ClientSerializer, WorkoutSessionSerializer
from rest_framework import viewsets
from .models import Gym, Trainer, Client, WorkoutSession
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated


# Create your views here.
class GymModelViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

class TrainerModelViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class ClientModelViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class WorkoutSessionModelViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
