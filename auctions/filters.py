from django_filters import rest_framework as filters, FilterSet, CharFilter
from .models import Item


class ItemApiFilter(filters.FilterSet):
    class Meta:
        model = Item
        fields = {
            "title": ['icontains'],
        }
