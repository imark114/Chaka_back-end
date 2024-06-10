from django.db import models
from product.models import Car
from account.models import User
# Create your models here.

class AddCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)