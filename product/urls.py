from django.urls import path,include
from product.views import ProductViewSet,CategoryViewSet
from rest_framework import routers
from .views import product_page
app_name='product'

router=routers.DefaultRouter()
router.register(r'category',CategoryViewSet)
router.register(r'product-list',ProductViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("",product_page,name="product-page"),
    # path("",)
]
 