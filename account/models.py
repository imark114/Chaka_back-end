from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='user')
    image = models.ImageField(upload_to='profile_images/', blank=True)

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.full_name