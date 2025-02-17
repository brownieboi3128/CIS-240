"""Defines URL patterns for code_journals."""

from django.urls import path

from . import views
app_name = 'code_journals'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    # Show all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
