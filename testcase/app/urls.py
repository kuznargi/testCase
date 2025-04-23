from django.urls import path
from .views import *


urlpatterns = [
    path('api/user/', UserCreateAPIView.as_view(), name='create_user'),
    path('api/courses/', CourseListAPI.as_view(), name='get_courses'),
    path('api/course/<int:pk>/', CourseDetailAPI.as_view(), name='get_course_data'),
    path('api/piano/', PianoListAPI.as_view(), name='get_piano'),
    path('api/note/', NoteDetailAPI.as_view(), name='get_note'),
    
    path('api/check-device/<str:device_id>/', DeviceCheckAPIView.as_view()),
    
    

]
