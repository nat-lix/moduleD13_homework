import django_filters
from django_filters import CharFilter, ModelChoiceFilter, DateFilter
from .models import Response, Category

from django import forms

class ResponseFilter(django_filters.FilterSet):
    dateCreation = django_filters.DateFilter(
        field_name='dateCreation',
        label='Дата создания позже чем',
        lookup_expr='gte',
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD-MM-YYYY'}),
    )
    responsePost__title = CharFilter(field_name='responsePost__title', label='Заголовок объявления', lookup_expr='icontains')
    responsePost__text = CharFilter(field_name='responsePost__text', label='Текст объявления',lookup_expr='icontains')
    responsePost__postCategory = ModelChoiceFilter(field_name='responsePost__postCategory', label='Категория объявления', lookup_expr='exact',
                                     queryset=Category.objects.all())

    class Meta:
        model = Response
        fields = ['dateCreation']