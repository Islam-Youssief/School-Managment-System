from django.urls import path, include
from .views import register, login, logout

app_name = 'students'

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]
