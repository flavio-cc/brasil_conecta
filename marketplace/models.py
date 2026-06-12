from django.db import models
class Category(models.Model):
    name=models.CharField(max_length=80)
    icon=models.CharField(max_length=12)
    color_class=models.CharField(max_length=30,default='green-soft')
    def __str__(self): return self.name
class ServiceProvider(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='services')
    name=models.CharField(max_length=120)
    city=models.CharField(max_length=80)
    province=models.CharField(max_length=40,default='ON')
    description=models.CharField(max_length=160)
    rating=models.DecimalField(max_digits=2,decimal_places=1,default=5.0)
    reviews=models.PositiveIntegerField(default=0)
    verified=models.BooleanField(default=True)
    whatsapp=models.CharField(max_length=30,blank=True)
    image_url=models.URLField(blank=True)
    def __str__(self): return self.name
class Product(models.Model):
    title=models.CharField(max_length=120)
    subtitle=models.CharField(max_length=120)
    city=models.CharField(max_length=80)
    province=models.CharField(max_length=40,default='ON')
    price=models.DecimalField(max_digits=8,decimal_places=2)
    image_url=models.URLField(blank=True)
    def __str__(self): return self.title
class CommunityGroup(models.Model):
    name=models.CharField(max_length=120)
    city=models.CharField(max_length=80,blank=True)
    members_label=models.CharField(max_length=40)
    icon=models.CharField(max_length=12)
    color_class=models.CharField(max_length=30)
    def __str__(self): return self.name
