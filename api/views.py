from django.shortcuts import render
from api.models import Room
from api.serializers import RoomSerializer
from rest_framework import generics

# Create your views here.

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


