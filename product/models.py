from django.db import models
import uuid
from django.template.defaultfilters import slugify
# Product Category
class Category(models.Model):
    name= models.CharField(max_length=100,null=False)
    slug=models.SlugField(default="", unique=True,null=False)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)+ '-' + uuid.uuid4().hex[:4]
        super(Category,self).save(*args, **kwargs)
    def __str__(self):
        return self.name
# Product Model
class Product(models.Model):
    category=models.ForeignKey("Category", on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    description=models.TextField(blank=True)
    quantity=models.IntegerField(default=0,null=False)
    image=models.ImageField(upload_to="products_img/",blank=True,null=True)
    price= models.DecimalField(default=0,max_digits=12, decimal_places=2)
    created_at=models.DateTimeField(null=True, auto_now_add=True)
    updated_at=models.DateTimeField(null=True, auto_now=True)
    slug=models.SlugField(default="",unique=True,null=False)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)+ '-' + uuid.uuid4().hex[:4]
        super(Product,self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    

