from django import forms
from .models import *

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['user', 'courses']
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Select User", widget=forms.Select(attrs={'class': 'form-control'}))
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),  
        label="Select Courses",
        widget=forms.CheckboxSelectMultiple 
    )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']