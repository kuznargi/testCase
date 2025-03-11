from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    courses = models.ManyToManyField(Course)  

    def __str__(self):  
        course_names = ", ".join([course.name for course in self.courses.all()])
        return f"Device Owner: {self.user.name}, Courses: {course_names if course_names else 'No Courses'}"

