import self as self
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import DateInput
from django.forms.utils import ErrorList

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

    # def clean(self):
    #     image = self.cleaned_data.get('profile_pic')
    #     # 5MB - 5242880
    #     if image.size > 50000:

def clean(profilepic):
    image = profilepic.size
          # 5MB - 5242880
    if image.size > 50000:
        raise ValidationError("KJHGTF")
    else:
        return image

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