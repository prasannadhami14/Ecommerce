from django.contrib import admin
from .models import Category,Product
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    # prepopulated_fields = {"slug":("name",)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['category','name','description','image','quantity','price']
    # prepopulated_fields = {"slug": ("name", "category","price")}
