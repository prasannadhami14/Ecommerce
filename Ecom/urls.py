
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('userApp.urls')),
    path('product/',include('product.urls')),
    path('orders/',include('orderApp.urls')),
    path('cart/',include('cartApp.urls'))


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
