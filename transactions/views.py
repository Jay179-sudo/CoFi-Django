from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import Transactions
from .forms import TransactionForm
class HomePageView(TemplateView):
    template_name="home.html"


class TransactionPageView(ListView):
    context_object_name = 'transaction_list'
    model = Transactions
    template_name = 'transactions.html'
    
    
class TransactionPageViewMonth(ListView):
    context_object_name = 'transaction_list'
    template_name = "transaction_month.html"
    paginate_by = 4
    def get_queryset(self):
        qs = Transactions.objects.all().filter(Transaction_Date__month=int(self.kwargs['month']))
        return qs

# Create your views here.
class TransactionDetailView(DetailView):
    model = Transactions
    template_name = "transaction_detail.html"

class TransactionDeleteView(DeleteView):
    model = Transactions
    template_name = "transaction_delete.html"
    success_url = reverse_lazy("home")


class PromiseCreateView(CreateView):
    model = Transactions
    form_class = TransactionForm
    template_name = "transaction_create.html"


# class TransactionCreateView(CreateView):
#     model = Transactions
#     template_name = "transaction_create.html"
#     fields = (
#         "Transaction_Detail",
#         "Amount",
#     )


class TransactionUpdateView(UpdateView):
    model = Transactions
    template_name="transaction_update.html"
    fields = (
        "Transaction_Detail",
        "Amount",
    )
