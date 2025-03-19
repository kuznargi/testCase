from rest_framework import serializers
from .models import *
from rest_framework import serializers    
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['device_id', 'age', 'courses']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'header', 'illustration']

class PianoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piano
        fields = ['note', 'time']
        