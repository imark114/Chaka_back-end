from django.contrib import admin
from .models import AddCart, Borrowing
# Register your models here.
@admin.register(AddCart)
class AddCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'car']

    def user(self, obj):
        return obj.user.username

    def car(self, obj):
        return obj.car.title

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['user', 'car', 'borrow_date']

    def user(self, obj):
        return obj.user.username

    def car(self, obj):
        return obj.car.title
