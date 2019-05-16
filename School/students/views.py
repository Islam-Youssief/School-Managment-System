from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm, LoginForm
from django.core.mail import send_mail
from .models import Student
from django.contrib import messages
import random


def register(request):
    if request.method == "GET":
        return render(request, "students/register.html", context={'form': StudentForm()})
    else:
        post_form = StudentForm(request.POST)
        if post_form.is_valid():
            student = post_form.save()
            student.username, student.password = generateEmailInfo(student)
            student.save()
            send_mail(
                'Activation Email For school managment system',
                'Hi {0},'.format(student.name) +
                '''Welcome to our site ,In order to access our site you need to use 
                username : {0} & password : {1}'''.format(
                    student.username, student.password),
                'islam.youssief@gmail.com', [student.email],
                fail_silently=False,
            )
        return redirect('students:login')
