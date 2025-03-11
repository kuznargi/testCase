from django.urls import path
from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('createUser', CreateUser.as_view(), name='createUser'),
    path('createDevice', CreateDevice.as_view(), name='createDevice'),
    path('createCourse', CreateCourse.as_view(), name='createCourse'),
    path('device/<int:pk>', DeviceDetail.as_view(), name='deviceDetail'),
    path('deleteDevice/<int:pk>', DeleteDevice.as_view(), name='deleteDevice'),

]
