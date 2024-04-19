#Specify the class that will convert the model into json compatible data
# Handle requests and convert them into json file in the background
from rest_framework import serializers
# from rest_framework import detection
from .models import detection

class detectionSerializers(serializers.ModelSerializers):
    class Meta:
        model = detection
        fields = '__all__'