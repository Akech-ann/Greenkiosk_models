from django.shortcuts import get_object_or_404, render

from Cartmanager.models import Cart
from .forms import ProductUploadForm
from inventory.models import Product
from django.shortcuts import redirect
#there are class based views and function based views
# Create your views here.
def upload_product(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = ProductUploadForm(request.POST, request.files)
        if form.is_valid():
            form.save()
    else:
        form = ProductUploadForm()
    return render(request, "inventory/product_upload.html", {"form": form})
def products_list(request):
    products = Product.objects.all()
    return render (request, "inventory/products_list.html", {"products": products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST" and "add_to_cart" in request.POST:
        cart = request.session.get('cart', [])
        cart.append(product.id)
        request.session['cart'] = cart
    return render(request, "inventory/product_detail.html", {"product": product})


def edit_product_view(request,id):
    product= Product.objects.get(id=id)
    if request.method =="POST":
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail_view", id = product.id)

    else:
        form = ProductUploadForm(instance=product)

    return render(request, 'inventory/edit_product.html',{"form":form})


def delete_product(request, id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect("products_list_view")
             
    
def cart_view(request):
    cart_product_ids = request.session.get('cart', [])
    cart_products = Product.objects.filter(id__in=cart_product_ids)
    return render(request, 'inventory/cart.html', {'cart_products': cart_products})

def add_to_cart(request, id):
    product = get_object_or_404(Product, pk=id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product.name,
        defaults={'price': product.price, 'quantity': 1, 'image': product.image}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

