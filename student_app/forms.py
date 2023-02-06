from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from student_app.models import Login, StudentRegister, AdminRegister, Mark


class DateInput(forms.DateInput):
    input_type = 'date'

class Login_Form(UserCreationForm):
    class Meta:
        model = Login
        fields = ("username","password1","password2")

class StudentRegisterForm(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)

    class Meta:
        model = StudentRegister
        fields = '__all__'
        exclude = 'user',

class AdminRegisterForm(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)

    class Meta:
        model = AdminRegister
        fields = '__all__'
        exclude = 'user',


class MarkForm(forms.ModelForm):

    class Meta:
        model = Mark
        fields = '__all__'