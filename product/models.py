from django.db import models
from account.models import User
from django.utils.text import slugify
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

MODE_CHOICE=[
    ('Auto', 'Auto'),
    ('Menual', 'Menual')
]

class Car(models.Model):
    title = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="car/images/")
    driving_mode = models.CharField(choices=MODE_CHOICE, max_length=20)
    speed= models.PositiveIntegerField()
    manufacture_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField()

    class Meta:
        permissions = [
            ("can_add_product", "Can add product"),
            ("can_change_product", "Can change product"),
            ("can_delete_product", "Can delete product"),
        ]

    def __str__(self):
        return self.title
    


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]


class Review(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    reviwer = models.ForeignKey(User,models.CASCADE)
    body = models.TextField()
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)