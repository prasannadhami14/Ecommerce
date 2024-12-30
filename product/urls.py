from django.urls import path,include
from product.views import ProductViewSet,CategoryViewSet
from rest_framework import routers
app_name='product'

router=routers.DefaultRouter()
router.register(r'category',CategoryViewSet)
router.register(r'product-list',ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("",)
]
 