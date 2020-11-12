from rest_framework import serializers

from .models import Category, Products, Order, Trdelnik


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class TrdelnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trdelnik
        fields = '__all__'
