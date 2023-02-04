from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from django.views.generic import TemplateView
from .models import Transactions

class HomePageView(TemplateView):
    template_name="home.html"


class TransactionPageView(ListView):
    context_object_name = 'transaction_list'
    queryset = Transactions.objects.filter(Transaction_Detail='trial')
    template_name = 'transaction_month.html'

    def get_queryset(self):
        order_by = self.request.GET.get('order_by') or '-created'
        qs = super().get_queryset()
        return qs.order_by(order_by)

class TransactionPageViewMonth(ListView):
    model = Transactions
    template_name = "transaction_month.html"

# Create your views here.
class TransactionDetailView(DetailView):
    model = Transactions
    template_name = "transaction_detail.html"

class TransactionDeleteView(DeleteView):
    model = Transactions
    template_name = "transaction_delete.html"
    success_url = reverse_lazy("home")

class TransactionCreateView(CreateView):
    model = Transactions
    template_name = "transaction_create.html"
    fields = (
        "Transaction_Detail",
        "Amount",
    )


class TransactionUpdateView(UpdateView):
    model = Transactions
    template_name="transaction_update.html"
    fields = (
        "Transaction_Detail",
        "Amount",
    )
