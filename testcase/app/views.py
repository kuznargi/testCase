from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from .models import User
class CourseDetailAPI(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        device_id = request.query_params.get('device_id')

        if not device_id or not User.objects.filter(device_id=device_id).exists():
            return Response({"detail": "Forbidden"}, status=403)

        return super().get(request, *args, **kwargs)
    
class CourseListAPI(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        device_id = request.query_params.get('device_id')

        if not device_id or not User.objects.filter(device_id=device_id).exists():
            return Response({"detail": "Forbidden"}, status=403)

        return super().get(request, *args, **kwargs)

class PianoListAPI(ListAPIView):
    queryset = Piano.objects.all()
    serializer_class = PianoSerializer

    def get(self, request, *args, **kwargs):
        device_id = request.query_params.get('device_id')

        if not device_id or not User.objects.filter(device_id=device_id).exists():
            return Response({"detail": "Forbidden"}, status=403)

        return super().get(request, *args, **kwargs)
    
class PianoDetailAPI(RetrieveAPIView):
    queryset = Piano.objects.all()
    serializer_class = PianoSerializer

    def get(self, request, *args, **kwargs):
        device_id = request.query_params.get('device_id')
        
        if not device_id:
            return Response(
                {"detail": "Device ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        if not User.objects.filter(device_id=device_id).exists():
            return Response(
                {"detail": "Invalid device ID"},
                status=status.HTTP_403_FORBIDDEN
            )
            
        return super().get(request, *args, **kwargs)
class NoteDetailAPI(ListAPIView):
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        device_id = self.request.query_params.get('device_id')
        note_ids = self.request.query_params.get('ids', '').split(',')
        
        if not device_id or not User.objects.filter(device_id=device_id).exists():
            return Note.objects.none()
            
        try:
            note_ids = [int(id) for id in note_ids if id.isdigit()]
            return Note.objects.filter(id__in=note_ids)
        except ValueError:
            return Note.objects.none()
class UserCreateAPIView(APIView):
 
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            device_id = serializer.validated_data.get('device_id')
            if User.objects.filter(device_id=device_id).exists():
                return Response(
                    {'error': 'Device already registered'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
class DeviceCheckAPIView(APIView):
  
    def get(self, request, device_id):
        exists = User.objects.filter(device_id=device_id).exists()
        return Response({'exists': exists})

 

 