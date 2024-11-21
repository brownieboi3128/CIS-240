from django.shortcuts import render
from . models import Transaction

# Create your views here.
def index(request):
    """The home page for budget_app."""
    return render(request, 'budget_app/index.html')

def transactions(request):
    """Show all transaction types."""
    transactions = Transaction.objects.order_by('date_added')
    context = {'transactions': transactions}
    return render(request, 'budget_app/transactions.html', context)

def transaction(request, transaction_id):
    """Show all transactions for a specific type."""
    transaction = Transaction.objects.get(id=transaction_id)
    entries = transaction.entry_set.order_by('-date_added')
    context = {'transaction': transaction, 'entries': entries}
    return render(request, 'budget_app/transaction.html', context)