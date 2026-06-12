from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('servicos/', views.services, name='services'),
    path('produtos/', views.products, name='products'),
    path('grupos/', views.groups, name='groups'),
]
