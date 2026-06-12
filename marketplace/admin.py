from django.contrib import admin
from .models import Category,ServiceProvider,Product,CommunityGroup
admin.site.register(Category)
admin.site.register(ServiceProvider)
admin.site.register(Product)
admin.site.register(CommunityGroup)
