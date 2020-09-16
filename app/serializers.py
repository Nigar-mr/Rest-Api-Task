from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Products, ProductsCategory


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsCategory

        fields = ['id', 'name']
        extra_kwargs = {'name': {'required': True}}


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        category = CategorySerializers(read_only=True)
        include_fk = True
        fields = ['id', 'category', 'name', 'count']
        extra_kwargs = {
            'category': {'required': True},
            'name': {'required': True},
            'count': {'required': True}
        }

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'count']

        def update(self, instance, validated_data):
            count = validated_data.get('count')
            prod = super(SaleSerializer, self).update(instance, validated_data)
            if count:
                prod.set_count(validated_data.get('count'))
            prod.save()
            return prod
