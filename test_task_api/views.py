
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from test_task_api.models import Products, Object
from test_task_api.serializers import ProductCreateSerializer, ProductSerializer, ObjectCreateSerializer, \
    ObjectSerializer


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


class ObjectCreateView(CreateAPIView):
    model = Object
    permission_classes = [IsAuthenticated]
    serializer_class = ObjectCreateSerializer


class ObjectListView(ListAPIView):
    model = Object
    permission_classes = [IsAuthenticated]
    serializer_class = ObjectCreateSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    ordering_fields = ["title", "created", "level", "arrears"]
    ordering = ["title", "level"]
    search_fields = [
        'title',
        "objects_type",
        "country",
        "arrears",
        "products",
    ]

    def get_queryset(self):
        return Object.objects.all()


class ObjectView(RetrieveUpdateDestroyAPIView):
    model = Object
    permission_classes = [IsAuthenticated]
    serializer_class = ObjectSerializer
    queryset = Object.objects.all()
