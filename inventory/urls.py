
from django.urls import path
from .views import upload_product ,products_list,product_detail,edit_product_view,delete_product,add_to_cart


urlpatterns= [
    path("product/upload",upload_product,name="product_upload_view"),
    path("products/list",products_list,name="products_list_view"),
    path("products/<int:id>/",product_detail,name="product_detail_view"),
    path("products/edit/<int:id>/", edit_product_view, name="product_edit_view"),
    path("products/delete/<int:id>/", delete_product, name="delete_product_view"),  
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
                            
]


    
