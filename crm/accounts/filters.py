import django_filters
from .models import *
from django_filters import CharFilter, DateFilter



class OrderFilter(django_filters.FilterSet):
    customer = CharFilter(field_name='customer__name', lookup_expr='icontains', label='Customer')
    product = CharFilter(field_name='product__name', lookup_expr='icontains', label='Product')
    start_date = DateFilter(field_name='date_created', lookup_expr='gte', label='Date from',)
    end_date = DateFilter(field_name='date_created', lookup_expr='lte', label='Date to',)

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'product', 'date_created']


class CustomerOrderFilter(django_filters.FilterSet):
    product = CharFilter(field_name='product__name', lookup_expr='icontains', label='Product')
    start_date = DateFilter(field_name='date_created', lookup_expr='gte', label='Date from', )
    end_date = DateFilter(field_name='date_created', lookup_expr='lte', label='Date to', )
    class Meta:
        model = Order
        fields = ['product', 'product__category', 'date_created', 'status']
        exclude = ['product', 'date_created']


