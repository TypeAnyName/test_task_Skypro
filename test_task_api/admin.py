from django.contrib import admin

from test_task_api.models import Products, Object


def make_arrears_done(modeladmin, request, queryset):
    for object_ in queryset:
        object_.arrears = 0.0
        object_.save()


make_arrears_done.short_description = "Отчистить долги"


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "model_of_product", "release")
    list_display_links = ('title',)
    search_fields = ("title",)


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "country",
        "products",
        "staff",
        "supplier",
        "arrears",
        "level"
    )
    list_display_links = ('title', 'supplier')
    search_fields = (
        "title",
        "objects_type",
        "country",
        "arrears",
        "products",
    )
    readonly_fields = ("created", "updated", "arrears")
    list_filter = ("country", "level", "arrears", "products")
    actions = [make_arrears_done, ]
