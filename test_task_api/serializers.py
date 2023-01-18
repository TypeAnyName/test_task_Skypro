from rest_framework import serializers

from core.models import User
from test_task_api.models import Products, Object


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ['id']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ObjectCreateSerializer(serializers.Serializer):
    class Meta:
        model = Object
        fields = "__all__"
        reads_only_fields = read_only_fields = ("id", "created", "updated", "staff")




