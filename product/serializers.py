from rest_framework import serializers
from .models import Product,Category
#create serializers
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
