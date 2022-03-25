from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    ordersCount = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers':customers, 'ordersCount':ordersCount, 'delivered':delivered,
               'pending':pending}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    orderCount = orders.count()
    context = {
        'customer':customer,
        'orders':orders,
        'orderCount':orderCount
    }
    return render(request, 'accounts/customer.html', context)