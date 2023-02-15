from datetime import date, datetime

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

from django.db import models



# Create your models here.

class Login(AbstractUser):
    is_adm = models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)


class StudentRegister(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    profile_pic = models.FileField(upload_to='profilepic/')
    dob = models.DateField(max_length=8)
    phone = models.CharField(max_length=10)

    def minimum_size(width=None, height=None):

        def validator(image):
            if not image.is_image():
                raise ValidationError('File should be image.')

            (errors, image_info) = ([], image.info()['image_info'])
            if width is not None and image_info['width'] < width:
                errors.append('Width should be > {} px.'.format(width))
            if height is not None and image_info['height'] < height:
                errors.append('Height should be > {} px.'.format(height))
            raise ValidationError(errors)

        return validator


    @property
    def age(self):
        return int((datetime.now().date() - self.dob).days /365.25)

    def __str__(self):
        return self.name




class AdminRegister(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    dob = models.DateField(max_length=8)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Mark(models.Model):
    name = models.ForeignKey(StudentRegister, on_delete=models.CASCADE)
    mark = models.IntegerField()

    def __str__(self):
        return self.name