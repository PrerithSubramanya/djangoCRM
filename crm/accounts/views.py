from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.core.paginator import Paginator
from .models import *
from .forms import OrderForm
from .filters import *
# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    ordersCount = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    customerPaginator = Paginator(customers,5)
    customerPageNum = request.GET.get('page')
    customerPage = customerPaginator.get_page(customerPageNum)
    myFilter = OrderFilter(request.GET, queryset=orders) # filterforms
    orders = myFilter.qs
    orderPaginator = Paginator(orders,5)
    orderPageNum = request.GET.get('page')
    orderPage = orderPaginator.get_page(orderPageNum)
    context = {'orderPage': orderPage, 'customerPage':customerPage, 'ordersCount':ordersCount, 'delivered':delivered,
               'pending':pending, 'myFilter':myFilter}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    orderCount = orders.count()

    myCustomerFilter = CustomerOrderFilter(request.GET, queryset=orders)
    orders = myCustomerFilter.qs

    context = {
        'customer':customer,
        'orders':orders,
        'orderCount':orderCount,
        'myCustomerFilter':myCustomerFilter
    }
    return render(request, 'accounts/customer.html', context)


def createOrder(request, id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=id)
    formset = OrderFormSet(queryset =Order.objects.none(), instance=customer) # queryset to display black on online forms
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.Post, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
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