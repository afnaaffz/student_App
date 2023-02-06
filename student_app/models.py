from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_adm = models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)

class StudentRegister(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    profile_pic = models.FileField(upload_to='profilepic/')
    dob = models.DateField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class AdminRegister(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    dob = models.DateField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Mark(models.Model):
    name = models.ForeignKey(StudentRegister, on_delete=models.CASCADE)
    mark = models.IntegerField()