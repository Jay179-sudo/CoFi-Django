from django import forms
from django.forms import ModelForm

from .models import Transactions


class DateInput(forms.DateInput):
    input_type = 'date'


class TransactionForm(ModelForm):

    class Meta:
        model = Transactions
        fields = ['Transaction_Detail', 'Amount', 'Transaction_Date']
        widgets = {
            'Transaction_Date': DateInput(),
        }