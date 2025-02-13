from .views import ProductList, ProductDetail,CategoryList, CategoryDetail
from django.urls import path


urlpatterns = [
    path('products', ProductList.as_view() , name='products_list'),
    path('products/<int:pk>', ProductDetail.as_view() , name='products_details'),
    path('categories', CategoryList.as_view(), name='categories_list'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='categories_details'),
]
