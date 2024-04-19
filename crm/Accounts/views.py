from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()

    totalCustomers = customer.count()

    totalOrders = orders.count()

    delivered = orders.filter(status="Delivered").count()

    pending = orders.filter(status="Pending").count()
    
    context = {"orders": orders, "customers": customer, "totalOrders": totalOrders, 
               "totalCustomers":totalCustomers, "delivered": delivered, "pending": pending}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/profile.html', {"products": products})

def customer(request):
    return render(request, 'accounts/customer.html' )