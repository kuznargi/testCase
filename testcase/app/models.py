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
class Note(models.Model):
    name = models.CharField(max_length=10)  
    
    def __str__(self):
        return self.name

class Piano(models.Model):
    time = models.CharField(max_length=255) 
    notes = models.ManyToManyField(Note) 
    
    def __str__(self):
        return f"Piano at {self.time} | Notes: {', '.join(str(note) for note in self.notes.all())}"





