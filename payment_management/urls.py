from django.urls import path
from .views import upload_payment,payment_detail,payments_list
urlpatterns = [
    path("payment_management/upload",upload_payment, name="payment_upload_view"),
    path("payment_management/list",payments_list, name = "payment_list_view"),
    path("payment_management/<int:id>/",payment_detail, name="payment_detail_view"),
]