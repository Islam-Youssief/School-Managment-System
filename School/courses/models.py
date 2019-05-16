from django.db import models
from django.db import IntegrityError
from students.models import Student


class Course(models.Model):
    """ represents the course itself."""
    name = models.CharField(max_length=50, blank=False, default='')
    days_needed = models.IntegerField(default=0)
    hours_needed = models.IntegerField(default=0)
    start_hour = models.TimeField(blank=True)
    end_hour = models.TimeField(blank=True)
    content = models.CharField(max_length=250)
    vacation = models.CharField(max_length=25)
    instructor_name = models.CharField(max_length=25)

    def save(self, *args, **kwargs):
        if not (self.end_hour > self.start_hour):
            raise IntegrityError
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class StudentCourses(models.Model):
    """ represents the relation between the student and his courses."""
    student = models.ForeignKey(Student, on_delete=True)
    course = models.ForeignKey(Course, on_delete=True)
