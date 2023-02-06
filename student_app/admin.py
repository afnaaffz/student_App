from django.contrib import admin

from student_app import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.StudentRegister)
admin.site.register(models.AdminRegister)
admin.site.register(models.Mark)