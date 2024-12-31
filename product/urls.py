from django.urls import path,include
from product.views import ProductViewSet,CategoryViewSet
from rest_framework import routers
from . import views
app_name='product'

router=routers.DefaultRouter()
router.register(r'category',CategoryViewSet)
router.register(r'product-list',ProductViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("",views.product_page,name="product-page"),
    path("product-details/<slug:slug>/",views.product_details,name="product-details")
    # path("",)
]
 