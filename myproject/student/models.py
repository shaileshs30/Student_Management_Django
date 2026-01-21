from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age= models.IntegerField()
    email= models. EmailField(unique=True)
    course = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Create your models here.

class StudentProfile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE
    )
    address = models.TextField()
    profile_image = models.ImageField(
        upload_to="",
        blank=True,
        null=True
    )
    def __str__(self):
        return self.student.name
