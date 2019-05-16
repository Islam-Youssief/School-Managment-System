from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from students.models import Student
from .models import Course, StudentCourses
import sweetify


def needed_context(request):
    all_courses = Course.objects.all()
    for onecourse in all_courses:
        student_courses = StudentCourses.objects.filter(
            course=onecourse.id, student=request.session['id'])
        if (student_courses):
            onecourse.reg = True
        else:
            onecourse.reg = False
    context = {
        'courses': all_courses,
    }
    return context


def info(request):
    if "id" not in request.session:
        return redirect('students:login')
    courses = Course.objects.all()
    return render(request, 'courses/showcourses.html', {'courses': courses})


def enrolled_courses(request):

    if "id" not in request.session:
        return redirect('students:login')
    return render(request, 'courses/enrolledcourses.html', needed_context(request))
