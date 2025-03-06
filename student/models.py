from django.db import models
from django.forms import ImageField


# Create your models here.
class Student(models.Model):
    image = models.ImageField(upload_to='student_images/',blank=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')))
    course = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Course(models.Model):
    name = models.CharField(max_length=20)
    course_code = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    subject_teaching = models.CharField(max_length=25)
    experience = models.CharField(max_length=15)

