from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from . models import *


class CreateLecturerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class CreateStudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class CreateAdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class StudentDetForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class ConsultationBooking(ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'

class LecturerDetForm(ModelForm):
    class Meta:
        model = Lecturer
        fields = '__all__'

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = '__all__'


