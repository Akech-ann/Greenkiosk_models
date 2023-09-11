from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect
# Create your views here.
from .forms import PaymentuploadForm
from payment_management.models import Payment
def upload_payment(request):
    if request.method == 'POST':
        # uploaded_payment = request.FILES["text"]
        form = PaymentuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PaymentuploadForm()
    return render(request, "payment/payment_upload.html", {"form": form})
def payments_list(request):
    payments = Payment.objects.all()
    return render (request, "payment/payment_list.html", {"payments": payments})
def  payment_detail(request,id):
  payment = Payment.objects.get(id =id)
  return render(request,"payment/payment_detail.html",{"payment":payment})