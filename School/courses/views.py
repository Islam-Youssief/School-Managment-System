from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from students.models import Student
from .models import Course, StudentCourses
import sweetify


def info(request):
    """ Get the info about all the courses"""
    if "id" not in request.session:
        return redirect('students:login')
    courses = Course.objects.all()
    return render(request, 'courses/showcourses.html', {'courses': courses})


def needed_context(request):
    """ Get all the needed context Cause it is needed in rendering a lot of pages."""
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


def enrolled_courses(request):
    """ Showing the enrolled courses and whether user whant to cancel his enrollments to courses."""
    if "id" not in request.session:
        return redirect('students:login')
    return render(request, 'courses/enrolledcourses.html', needed_context(request))


def send_reminder(request):
    """ Send email of enrollment courses"""
    # preparing the data to be sent
    student = Student.objects.filter(id=request.session['id'])
    student_courses = StudentCourses.objects.filter(
        student=request.session['id'])
    info = {}
    allinfo = []
    for studentinfo in student_courses:
        # feeding up info with data
        info['Course Name'] = studentinfo.course.name
        info['Duration In Days'] = studentinfo.course.days_needed
        info['Duration In Hours'] = studentinfo.course.hours_needed
        info['Starting Hour'] = studentinfo.course.start_hour
        info['Ending Hour'] = studentinfo.course.end_hour
        info['Course Description'] = studentinfo.course.content
        info['Vacation Day'] = studentinfo.course.vacation
        info['Instructor Name'] = studentinfo.course.instructor_name
        allinfo.append(info.copy())
    # The actual function of sending emails
    send_mail(
        'Reminder Of All Your Enrolled Courses',
        'Hi {0},'.format(student[0].name) +
        """\nThis is a reminder of all the enrolled courses in our platform : \n
            ~~ please make sure of your schudle and be on time ^_^ ~~ \n{0}""".format(allinfo),
        'developer.islam.youssief@gmail.com', [student[0].email],
        fail_silently=False,
    )
    messages.info(request, 'Your Info was sent to your email successfully!')
    return render(request, 'courses/enrolledcourses.html',
                  needed_context(request))


def register(request, pk):
    """ Enroll to new course."""
    if "id" not in request.session:
        return redirect('students:login')
    course = get_object_or_404(Course, pk=pk)
    student = get_object_or_404(Student, pk=request.session['id'])
    StudentCourses(student=student, course=course).save()
    return render(request, 'courses/enrolledcourses.html', needed_context(request))


def unregister(request, pk):
    """ Cancel enrollment of any registered course."""
    if "id" not in request.session:
        return redirect('students:login')
    course = get_object_or_404(Course, pk=pk)
    student = get_object_or_404(Student, pk=request.session['id'])
    get_object_or_404(StudentCourses, student=student, course=course).delete()
    return render(request, 'courses/enrolledcourses.html', needed_context(request))
