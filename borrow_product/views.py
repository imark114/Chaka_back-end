from django.shortcuts import render
from .serializers import AddCartSerializer, BorrowSerializer
from .models import AddCart, Borrowing
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BorrowViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Borrowing.objects.all()
    serializer_class = BorrowSerializer
    

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset

class AddCartViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AddCart.objects.all()
    serializer_class = AddCartSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'status': 'success',
            'message': 'Product Added to Your Cart List',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset