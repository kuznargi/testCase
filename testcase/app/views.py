from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Course
from .serializers import UserSerializer
from django.template.loader import render_to_string

class SurveyView(APIView):
  
    def post(self, request, *args, **kwargs):
        device_id = request.data.get('device_id')
        age = request.data.get('age')
        needed_courses_ids = request.data.get('needed_courses_ids')

  
        user, created = User.objects.get_or_create(device_id=device_id, defaults={'age': age})

       
        if needed_courses_ids:
            courses = Course.objects.filter(id__in=needed_courses_ids)
            user.courses.set(courses)

        user.save()
        return Response({"message": "Survey created successfully", "user": UserSerializer(user).data}, status=status.HTTP_201_CREATED)
    
class CoursesView(APIView):
    def get(self, request, *args, **kwargs):
        device_id = request.query_params.get('device_id')
        if device_id:
            user = User.objects.get(device_id=device_id)
            courses = user.courses.all()
            courses_data = [{"course_id": course.id, "header": course.header, "illustration": course.illustration} for course in courses]
            return Response(courses_data)
        return Response({"error": "Device ID is required"}, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    def get(self, request, *args, **kwargs):
        course_id = request.query_params.get('course_id')
        if course_id:
            course = Course.objects.get(id=course_id)
            html_content = render_to_string('course_template.html', {'course': course})
            return Response({"html": html_content})
        return Response({"error": "Course ID is required"}, status=status.HTTP_400_BAD_REQUEST)

class PianoParamsView(APIView):
    """
    GET request to return piano parameters based on piano_id.
    """
    def get(self, request, *args, **kwargs):
        piano_id = request.query_params.get('piano_id')
        if piano_id:
            try:
                piano = Piano.objects.get(id=piano_id)
                piano_data = {"note": piano.note, "time": piano.time}
                return Response(piano_data)
            except Piano.DoesNotExist:
                return Response({"error": "Piano parameters not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "Piano ID is required"}, status=status.HTTP_400_BAD_REQUEST)
