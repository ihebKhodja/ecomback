from django.shortcuts import render
from rest_framework.views import APIView
from .models import Cart
from .serializers import CartSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CartList(APIView):
    
    def post(self, request):
        serializer= CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartByUser(APIView):
    def get(self, request, pk):
        cart = Cart.objects.filter(user=pk)
        if not cart.exists():
            return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)        
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
    

class CartDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        cart = self.get_obj_by_user(pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    def put(self, request, pk):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        cart = self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)