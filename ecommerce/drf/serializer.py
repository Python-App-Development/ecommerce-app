from attr import field
from ecommerce.inventory.models import Product, ProductInventory
from rest_framework import serializers


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = "__all__"
        # fields = ["name"]
        exclude = ["id"]
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = "__all__"
        read_only = True
        depth = 3
