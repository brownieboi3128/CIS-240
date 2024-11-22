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
    #Page for adding a new topic
	path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	# Page for displaying a bar chart
	path('bar_chart/', views.bar_chart, name='bar_chart'),
]