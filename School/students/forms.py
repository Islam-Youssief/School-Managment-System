from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
	"""This Class represents registeration form"""
    class Meta:
        model = Student
        fields = ('name', 'email', 'birthdate', 'phone')


class LoginForm(forms.ModelForm):
	"""This Class represents lgoin form"""
    class Meta:
        model = Student
        fields = ('username', 'password')
