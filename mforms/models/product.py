from django.db import models
from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    image=models.ImageField(upload_to='uploads', default='mforms/static/images/default_img.png')