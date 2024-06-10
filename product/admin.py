from django.contrib import admin
from .models import Brand, Car, Review
# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'driving_mode', 'price']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['car', 'reviwer', 'rating']

    def car(self, obj):
        return obj.car.title
    
    def reviwer(self, obj):
        return obj.reviwer.username

