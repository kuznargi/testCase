from django.db import models

class User(models.Model):
    device_id = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
    courses = models.ManyToManyField('Course', blank=True)  

    def __str__(self):
        return f"User {self.device_id}"


class Course(models.Model):
    header = models.CharField(max_length=255)
    illustration = models.URLField()
    def __str__(self):
        return self.header
    

class Piano(models.Model):
    note = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

    def __str__(self):
        return self.note
    



