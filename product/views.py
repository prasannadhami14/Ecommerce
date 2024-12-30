from rest_framework import viewsets
from product.models import Product,Category
from product.serializers import ProductSerializers, CategorySerializers
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
   queryset=Category.objects.all()
   serializer_class=CategorySerializers

class ProductViewSet(viewsets.ModelViewSet):
   queryset=Product.objects.all()
   serializer_class=ProductSerializers

