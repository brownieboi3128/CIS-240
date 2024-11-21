from django.db import models

# Create your models here.
class Transactions(models.Model):
    TransactionType = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return str(self.TransactionType)
    
class Entry(models.Model):
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    merchant = models.CharField(max_length=200)
    description = models.TextField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
#    def __str__(self):
#        """Return a string representation of the model"""
#        return str(self.transaction)
    

    def __str__(self):
        """Return a string representation of the merchant information"""
        return str(self.merchant) + " " + str(self.transaction_amount)
