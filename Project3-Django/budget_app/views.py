from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . models import Transaction
from . forms import EntryForm
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components

# Create your views here.
def index(request):
    """The home page for budget_app."""
    return render(request, 'budget_app/index.html')

def transactions(request):
    """Show all transaction types."""
    transactions = Transaction.objects.order_by('date_added')
    context = {'transactions': transactions, 'other_transactions': ['transactions']}
    return render(request, 'budget_app/transactions.html', context)

def transaction(request, transaction_id):
    """Show all transactions for a specific type."""
    transaction = Transaction.objects.get(id=transaction_id)
    entries = transaction.entry_set.order_by('-date_added')
    context = {'transaction': transaction, 'entries': entries}
    return render(request, 'budget_app/transaction.html', context)

def new_entry(request, transaction_id):
    """Add a new entry for a particular transaction type."""
    transaction = Transaction.objects.get(id=transaction_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.transaction = transaction
            new_entry.save()
            return HttpResponseRedirect(reverse('budget_app:transaction', args=[transaction_id]))
    
    context = {'transaction': transaction, 'form': form}
    return render(request, 'budget_app/new_entry.html', context)

def bar_chart(request):
    """Display a bar chart."""
    transactions = Transaction.objects.order_by('date_added')
    transaction_entry_count = [(transaction.id, transaction.entry_set.count()) for transaction in transactions]
    df = pd.DataFrame(transaction_entry_count, columns=['transactions', 'Entry Count'])
    # instantiate a figure object
    fig = figure(x_range=[str(x) for x in df['transactions']], title='Transaction Entry Count', height=500, width=700)
    #create the bar chart
    fig.vbar(source=df, x='transaction', top='Entry Count', width=0.9, color='purple')
    html, div = components(fig)
    context = {'html': html, 'div': div}
    return render(request, 'budget_app/bar_chart.html', context)