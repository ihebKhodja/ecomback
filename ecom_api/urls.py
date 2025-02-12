from .views import ProductList, ProductDetail,CategoryViewSet
from django.urls import path


urlpatterns = [
    path('products', ProductList.as_view() , name='products_list'),
    path('products/<int:pk>', ProductDetail.as_view() , name='products_details'),
    path('categories', CategoryViewSet.as_view({'get':'list'}), name='categories'),
]
