from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from rest_framework.response import Response
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

class NoteListAPI(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        device_id = request.query_params.get('device_id')

        if not device_id or not User.objects.filter(device_id=device_id).exists():
            return Response({"detail": "Forbidden"}, status=403)

        return super().get(request, *args, **kwargs)
class UserCreateAPI(CreateAPIView):
     queryset=User.objects.all()
     serializer_class=UserSerializer
 

 