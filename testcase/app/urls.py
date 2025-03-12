from django.urls import path
from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('createUser', CreateUser.as_view(), name='createUser'),
    path('createDevice', CreateDevice.as_view(), name='createDevice'),
    path('createCourse', CreateCourse.as_view(), name='createCourse'),
    path('device/<int:pk>', DeviceDetail.as_view(), name='deviceDetail'),
    path('deleteDevice/<int:pk>', DeleteDevice.as_view(), name='deleteDevice'),
    path('api/createDevice/', DeviceCreateAPI.as_view(), name='createDeviceAPI'),
    path('api/device/<pk>',DeviceDetailAPI.as_view(),name='detailDeviceAPI'),
    path('api/device/list/',DeviceListAPI.as_view(),name='deviceListAPI'),
    path('api/createUser/', UserCreateAPI.as_view(), name='createUserAPI'),
    path('api/user/<pk>',UserDetailAPI.as_view(),name='detailUserAPI'),
    path('api/user/list/',UserListAPI.as_view(),name='userListAPI'),
    path('api/createCourse/', CourseCreateAPI.as_view(), name='createDeviceAPI'),
    path('api/course/<pk>',CourseDetailAPI.as_view(),name='detailDeviceAPI'),
    path('api/course/list/',CourseListAPI.as_view(),name='deviceListAPI'),
  
]
