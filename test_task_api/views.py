from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from test_task_api.models import Products
from test_task_api.serializers import ProductCreateSerializer, ProductSerializer


class ProductsCreateView(CreateAPIView):
    model = Products
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCreateSerializer


class ProductsListView(ListAPIView):
    model = Products
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    ordering_fields = ["title", "release"]
    ordering = ["title"]
    search_fields = ['title']

    def get_queryset(self):
        return Products.objects.all()


class ProductsView(RetrieveUpdateDestroyAPIView):
    model = Products
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
