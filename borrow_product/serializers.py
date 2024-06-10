from rest_framework import serializers
from .models import AddCart, Borrowing

class AddCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCart
        fields = '__all__'

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = '__all__'