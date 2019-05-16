from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    path('info', info, name="info"),
    path('allcourses', enrolled_courses),
    path('register/<int:pk>', register, name='register'),
    path('unregister/<int:pk>', unregister, name='unregister'),
    path('sendmail', send_reminder, name="send_reminder")
]
