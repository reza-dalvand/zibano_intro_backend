"""
URL configuration for website app.
"""

from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/contact/', views.submit_contact, name='submit_contact'),
]