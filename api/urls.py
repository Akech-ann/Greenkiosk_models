from django.urls import path
from .views import CustomerListView,CustomerDetailView,OrderDetailView,OrderListView

urlpatterns= [
    path("customers/", CustomerListView.as_view(), name= "customer_list_view"),
    path("customers/<int:id>/",CustomerDetailView.as_view(), name="customer_detail"),
    path("order_management/",OrderListView.as_view(),name="order_list_view"),
    path("order_management/<int:id>/",OrderDetailView.as_view(),name="order_detail.view"),
]

