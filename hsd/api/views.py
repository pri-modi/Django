from django.shortcuts import render
from rest_framework import generics
from .models import speechDetection
from .serializers import speechDetectionSerializer

# Create your views here.

class speechDetectionListCreate(generics.ListCreateAPIView):
    queryset = speechDetection.objects.all()
    serializer_class = speechDetectionSerializer
