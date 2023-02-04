from django.urls import path
from .views import HomePageView, TransactionPageView, TransactionCreateView, TransactionDetailView, TransactionUpdateView, TransactionDeleteView, TransactionPageViewMonth
urlpatterns = [
path("", HomePageView.as_view(), name="home"),
path("transactions/", TransactionPageView.as_view(), name='transactions'),
path("transactions_month/", TransactionPageViewMonth.as_view(), name='transactions_month'),
path("transactions/add/", TransactionCreateView.as_view(), name='add'),
path("transactions/delete/<int:pk>", TransactionDeleteView.as_view(), name='delete'),
path("transactions/update/<int:pk>", TransactionUpdateView.as_view(), name='update'),
path("transactions/detail/<int:pk>", TransactionDetailView.as_view(), name='detail'),
]
