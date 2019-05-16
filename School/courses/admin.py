from django.contrib import admin
from .models import Course, StudentCourses

# represents the course itself
admin.site.register(Course)
# represents the relation between the student and his courses
admin.site.register(StudentCourses)
