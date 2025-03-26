from rest_framework import serializers
from .models import *
from rest_framework import serializers    
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class PianoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piano
        fields = '__all__'
        
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        
        