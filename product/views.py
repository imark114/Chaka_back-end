from django.shortcuts import render
from .models import Car, Brand,Review
from .serializers import CarSerializer, BrandSerializer,ReviewSerializer
from account.permissions import IsSuperAdmin, IsAdmin, IsUser
from rest_framework import viewsets,filters
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'brand__name']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated,IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated,IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]



class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        car_id = self.request.query_params.get('car_id')
        reviewer_id = self.request.query_params.get('reviewer_id')
        if car_id:
            queryset = queryset.filter(car_id=car_id)
        if reviewer_id:
            queryset = queryset.filter(reviewer_id=reviewer_id)

        return queryset
