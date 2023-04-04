from django_filters import rest_framework as filters
from .models import CartNews

class CartNewsFilter(filters.FilterSet):
    title = filters.CharFilter('title', 'icontains')