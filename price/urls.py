from django.urls import path, include, re_path
from price.apps import PriceConfig
from price.views import ProductViewSet, CustomUserViewSet
from rest_framework.routers import DefaultRouter
app_name = PriceConfig.name
###, CategoryViewSet, про Пользователей и Категории в задании нет упоминания, пока закомментирую


router = DefaultRouter()
router.register(r'price', CustomUserViewSet, basename='price')
# router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')

urlpatterns = [
               path('', ProductViewSet.as_view({'get': 'list'}), name='product_list'),
               path('product_create/', ProductViewSet.as_view({'post': 'create'}), name='product_create'),
               path('product_detail/<int:pk>', ProductViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'}), name='product_detail'),
               path('CustomUserList/', CustomUserViewSet.as_view({'get': 'list'}), name='product_list'),
               path('CustomUser_detail/<int:pk>', CustomUserViewSet.as_view({
                                            'get': 'retrieve',
                                            'put': 'update',
                                            'patch': 'partial_update',
                                            'delete': 'destroy'}), name='product_detail'),

               ] + router.urls

