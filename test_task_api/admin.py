from django.contrib import admin

from test_task_api.models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "model_of_product", "release")
    list_display_links = ('title',)
    search_fields = ("title",)
