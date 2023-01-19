from django.urls import path

from test_task_api import views

urlpatterns = [
    path("product/create", views.ProductsCreateView.as_view(), name="creat-product"),
    path("product/list", views.ProductsListView.as_view(), name="products-list"),
    path("product/<pk>", views.ProductsView.as_view(), name="products-detail"),

    path("object/create", views.ObjectCreateView.as_view(), name="object-create"),
    path("object/list", views.ObjectListView.as_view(), name="object-list"),
    path("object/<pk>", views.ObjectView.as_view(), name="object-detail"),
]
