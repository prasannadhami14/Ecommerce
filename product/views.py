from rest_framework import viewsets
from product.models import Product,Category
from product.serializers import ProductSerializers, CategorySerializers
from django.shortcuts import render
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
   queryset=Category.objects.all()
   serializer_class=CategorySerializers

class ProductViewSet(viewsets.ModelViewSet):
   queryset=Product.objects.all()
   serializer_class=ProductSerializers

def product_page(request):
   products=Product.objects.all()
   product_det={
      "products":products,
   }
   return render(request,'productApp/index.html',product_det)