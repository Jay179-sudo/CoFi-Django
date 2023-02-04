from django.db import models
from django.urls import reverse

# Create your models here.
class Transactions(models.Model):
    primary_id = models.BigAutoField(primary_key=True, auto_created=True)
    Transaction_Detail = models.CharField(max_length=200)
    Amount = models.DecimalField(max_digits=6, decimal_places=2)
    Transaction_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Transaction_Detail[:50]
    
    def get_absolute_url(self):
        return reverse("transactions")