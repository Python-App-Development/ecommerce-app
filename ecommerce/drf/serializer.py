from attr import field
from ecommerce.inventory.models import (
    Brand,
    Media,
    Product,
    ProductAttributeValue,
    ProductInventory,
)
from rest_framework import serializers


class MediaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["image", "is_feature"]
        read_only = True

    def get_image(self, obj):
        return self.context["request"].build_absolute_uri(obj.image.url)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "name",
        ]
        read_only = True


# , "product_attribute__description"
class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        exclude = ["id"]
        read_only = True
        depth = 2


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = "__all__"
        # fields = ["name"]
        exclude = ["id"]
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    attribute = ProductAttributeValueSerializer(
        source="attribute_values", many=True, read_only=True
    )
    image = MediaSerializer(
        source="media_product_inventory", many=True, read_only=True
    )

    class Meta:
        model = ProductInventory
        fields = [
            "sku",
            "store_price",
            "image",
            "is_default",
            "product",
            "product_type",
            "brand",
            "attribute",
        ]
        read_only = True
