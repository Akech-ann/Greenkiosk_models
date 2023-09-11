from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('name','total','number_of_products','shipping_cost','payment_options', 'discount')

    def display_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])

    display_products.short_description = 'Products'

admin.site.register(Cart, CartAdmin)


