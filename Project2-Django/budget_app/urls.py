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
]