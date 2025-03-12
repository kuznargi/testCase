from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView

class DeviceListAPI(ListAPIView):
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer

class DeviceCreateAPI(CreateAPIView):
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer

class DeviceDetailAPI(RetrieveAPIView):
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer

class CourseListAPI(ListAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class CourseCreateAPI(CreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class CourseDetailAPI(RetrieveAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class UserListAPI(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserCreateAPI(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetailAPI(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class CreateDevice(CreateView):
    model=Device
    form_class=DeviceForm
    template_name='createDevice.html'
    success_url=reverse_lazy('main')

class MainView(ListView):
    model=Device
    template_name='main.html'
    context_object_name='devices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['courses'] = Course.objects.all()

        return context


class CreateUser(CreateView):
    model=User
    form_class=UserForm
    template_name='createUser.html'
    success_url=reverse_lazy('main')
    

class CreateCourse(CreateView):
    model=Course
    form_class=CourseForm
    template_name='createCourse.html'
    success_url=reverse_lazy('main')

class DeviceDetail(DetailView):
    model=Device
    template_name='deviceDetail.html'
    context_object_name='device'

class DeleteDevice(DeleteView):
    model=Device
    template_name='delete.html'
    success_url=reverse_lazy('main')
