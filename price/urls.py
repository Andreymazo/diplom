from django.urls import path, include
from django.contrib import admin

from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from price import views
from rest_framework import routers

from price.apps import PriceConfig
from price.views import CustomUserViewSet, CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter
app_name = PriceConfig.name

router = DefaultRouter()
router.register(r'price', CustomUserViewSet, basename='price')
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')

urlpatterns = [
               path('product_list/', ProductViewSet.as_view({'get': 'list'}), name='product_list'),
               path('product_create/', ProductViewSet.as_view({'post': 'create'}), name='product_create'),
               path('product_detail/<int:pk>', ProductViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'}), name='product_detail'),
               ] + router.urls

