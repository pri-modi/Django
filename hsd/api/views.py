from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import speechDetection
from .serializers import speechDetectionSerializer

# Create your views here.

class speechDetectionListCreate(generics.ListCreateAPIView):
    queryset = speechDetection.objects.all()
    serializer_class = speechDetectionSerializer

    def delete(self, request, *args, **kwargs):
        speechDetection.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)