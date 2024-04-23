# urls.py
from django.urls import path
from . import register

urlpatterns = [
    path('register/', register.register, name='register'),
    # Add other URL patterns as needed
]
