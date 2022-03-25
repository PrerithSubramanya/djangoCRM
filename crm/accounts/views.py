from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
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


def createOrder(request, id):
    customer = Customer.objects.get(id=id)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/createOrder.html', context)

def updateOrder(request, id):
    order = Order.objects.get(id=id)

    form = OrderForm(instance=order) #pass in the instance value to modify the order instance picked by id
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/createOrder.html', context)


def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    if request.method =='POST':
        order.delete()
        return redirect('/')
    context = {'order': order}
    return render(request, 'accounts/deleteOrder.html', context)