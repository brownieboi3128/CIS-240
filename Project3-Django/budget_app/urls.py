"""Defines URL patterns for budget_app."""

from django.urls import path
from . import views

app_name = 'budget_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all transaction types
    path('transactions/', views.transactions, name='transactions'),
    #page that shows all transactions for a specific type
    path('transactions/<int:transaction_id>/', views.transaction, name='transaction'),
    #page that shows the form to add a new entry
    path('new_entry/<int:transaction_id>/', views.new_entry, name='new_entry'),
    #page for displaying a bar chart
    path('bar_chart/', views.bar_chart, name='bar_chart'),
]