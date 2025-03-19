from django.db import models


class User(models.Model):
    name=models.CharField(max_length=255)
    device_id = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
  
    def __str__(self):
        return f"User {self.device_id}"


class Course(models.Model):
    header = models.CharField(max_length=255)
    illustration = models.URLField()
    description = models.TextField()
    def __str__(self):
        return self.header
    

class Piano(models.Model):
    note = models.CharField(max_length=255)
    time = models.CharField(max_length=255)

    def __str__(self):
        return self.note
    



