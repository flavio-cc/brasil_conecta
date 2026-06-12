from django.contrib import admin
from .models import Category, ServiceProvider, Product, CommunityGroup

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'service_count')

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'city', 'verified', 'featured', 'rating')
    list_filter = ('verified', 'featured', 'category', 'city')
    search_fields = ('name', 'description', 'city')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'city')
    search_fields = ('title', 'city')

@admin.register(CommunityGroup)
class CommunityGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'members')
    search_fields = ('name', 'city')
