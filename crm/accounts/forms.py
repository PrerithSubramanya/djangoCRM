from django.forms import ModelForm, widgets
from .models import *
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']
        exclude = ['dateCreated']
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control', 'type':'tel'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'tags']
        exclude = ['dateCreated']
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'tags':forms.SelectMultiple(attrs={'class': 'form-control'})
        }