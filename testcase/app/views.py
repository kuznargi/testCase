from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from .models import *
from .forms import *


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
