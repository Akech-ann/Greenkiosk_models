from .views import cart_upload_form,cart_list,cart_detail,edit_cart_view
from django.urls import path



urlpatterns=[
    path('Cartmanager/upload', cart_upload_form, name='cart_upload_view'),
    path('Cartmanager/list', cart_list, name='cart_list_view'),
    path("Cartmanager/<int:id>/",cart_detail,name="cart_detail_view"),
    path("Cartmanager/edit/<int:id>/", edit_cart_view, name="cart_edit_view")
    

]

