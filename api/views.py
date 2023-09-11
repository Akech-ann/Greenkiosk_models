from rest_framework.views import APIView
from customer_management.models import Customer
from .serializers import CustomerSerializer,OrderSerializer
from rest_framework import status
from rest_framework.response import Response
from order_management.models import Order

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailView(APIView):
    def get(self, request,id, format = None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self, request, id, format = None):
        customer = Customer.objects.get(id = id)
        serializer = CustomerSerializer(customer, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id , format = None):
        customer = Customer.objects.get(id = id)
        customer.delete
        return Response("customer deleted",status= status.HTTP_204_NO_CONTENT)



# apis for order

class OrderListView(APIView):
    def get(self,request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
class OrderDetailView(APIView):
    def get(self,request,id,format = None):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    def put (self, request,id,format =None):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format = None):
        order = Order.objects.get(id=id)
        order.delete()
        return Response("order deleted", status=status.HTTP_204_NO_CONTENT)