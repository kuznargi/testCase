from django.urls import path
from .views import *


urlpatterns = [
    path('api/survey/', SurveyView.as_view(), name='create_survey'),
    path('api/courses/', CoursesView.as_view(), name='get_courses'),
    path('api/course/', CourseDetailView.as_view(), name='get_course_data'),
    path('api/piano/', PianoParamsView.as_view(), name='get_piano_params'),

]
