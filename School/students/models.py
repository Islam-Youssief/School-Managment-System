from django.db import models
from django.core.validators import RegexValidator


class Student(models.Model):

    name_regex = RegexValidator(regex=r'^([A-Za-z])+$',
                                message="Please enter a valid name")
    username = models.CharField(
        max_length=45, blank=False)
    name = models.CharField(max_length=45, blank=False,
                            validators=[name_regex])
    email_regex = RegexValidator(regex=r'^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$',
                                 message="Please enter a valid email address")
    email = models.EmailField(
        max_length=45, blank=False, validators=[email_regex])
    password = models.CharField(max_length=45, blank=False)
    birthdate = models.DateTimeField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^01[5|1|2|0][0-9]{8}$',
                                 message="Please enter a valid phone number")
    phone = models.CharField(max_length=11,
                             validators=[phone_regex], blank=True)
