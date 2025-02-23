from .views import CartList, CartDetail, CartByUser
from django.urls import path

urlpatterns = [
    path('cart', CartList.as_view(), name='cart_list'),
    path('cart/<int:pk>', CartDetail.as_view(), name='cart_details'),
    path('cart/user/<int:pk>', CartByUser.as_view(), name='cart_by_user'),
]
