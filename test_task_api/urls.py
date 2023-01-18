from django.urls import path

from test_task_api import views

urlpatterns = [
    path("product/create", views.ProductsCreateView.as_view(), name="creat-product"),
    path("product/list", views.ProductsListView.as_view(), name="products-list"),
    path("product/<pk>", views.ProductsView.as_view(), name="products-detail"),
]