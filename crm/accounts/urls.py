from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:id>', views.customer, name='customer'),
    path('createOrder/<str:id>', views.createOrder, name='createOrder'),
    path('updateOrder/<str:id>', views.updateOrder, name='updateOrder'),
    path('deleteOrder/<str:id>', views.deleteOrder, name='deleteOrder'),
]