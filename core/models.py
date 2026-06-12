from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80)
    icon = models.CharField(max_length=12, default='🇧🇷')
    service_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class ServiceProvider(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=80)
    province = models.CharField(max_length=40, default='QC')
    whatsapp = models.CharField(max_length=30, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    review_count = models.PositiveIntegerField(default=0)
    verified = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.CharField(max_length=80)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class CommunityGroup(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=80, blank=True)
    members = models.PositiveIntegerField(default=0)
    icon = models.CharField(max_length=12, default='👥')

    def __str__(self):
        return self.name
