from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=200)
    grades = models.CharField(max_length=200)
    average_grade = models.FloatField(max_length=200)

