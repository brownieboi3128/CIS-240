from django.db import models

# Create your models here.
class transactions(models.Model):
    """A transaction the user wants to record info about"""
    TransactionType = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return str(self.TransactionType)