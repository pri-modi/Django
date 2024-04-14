#Specify the class that will convert the model into json compatible data
from rest_framework import serializers
from .models import speechDetection

class speechDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = speechDetection
        fields = ["text"]