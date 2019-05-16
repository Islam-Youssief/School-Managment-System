from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm, LoginForm
from django.core.mail import send_mail
from .models import Student
from django.contrib import messages
import random


def register(request):
    """ Register New User."""
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


def login(request):
    """ Login using email and passowrd sent by email"""
    if request.method == "GET":
        return render(request, "students/login.html", context={'form': LoginForm()})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            students = Student.objects.filter(username=form.cleaned_data['username'],
                                              password=form.cleaned_data['password'])
            if (students):
                request.session['id'] = students[0].id
                return redirect('courses:info')
            else:
                messages.error(request, 'username or password not correct')
                return redirect('students:login')


def logout(request):
    """ Logout and delete the session"""
    if "id" not in request.session:
        return redirect('students:login')
    del request.session['id']
    return redirect('students:login')


def generateEmailInfo(student):
    """ Generate username and password sent by email"""
    return(''.join(student.name[:4] + student.email[:4] + student.phone[:4] + str(random.randint(1, 101))),
           ''.join(student.name[-4:] + student.email[-4:] + student.phone[-4:] + str(random.randint(1, 101))))
