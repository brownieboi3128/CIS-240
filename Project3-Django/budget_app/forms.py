from django import forms 

from . models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['merchant', 'description', 'transaction_amount']
        labels = {'merchant': "Merchant", 'description': 'Description', 'transaction_amount':'Transaction amount'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}