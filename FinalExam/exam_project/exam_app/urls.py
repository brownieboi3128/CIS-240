"""Defines URL patterns for exam_app."""

from django.urls import path

from . import views
app_name = 'exam_app'
urlpatterns = [
    #home page
    path('', views.bar_chart, name='bar_chart'),
]