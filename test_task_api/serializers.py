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


class ObjectCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        object_ = Object.objects.create(**validated_data)

        if object_.object_type == 1:
            pass
        else:
            if object_.supplier.level == 0:
                object_.level += 1
            elif object_.supplier.level == 1:
                object_.level += 2
            elif object_.supplier.level == 2:
                object_.level += 3
            elif object_.supplier.level == 3:
                object_.level += 4
            elif object_.supplier.level == 4:
                object_.level += 5
            elif object_.supplier.level == 5:
                pass

        object_.save()
        return object_

    class Meta:
        model = Object
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", 'level')


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", 'level', "arrears")
