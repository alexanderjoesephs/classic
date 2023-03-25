from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class User(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    year = models.IntegerField()
    image_link = models.ImageField(upload_to="images/")
    price = models.FloatField() 
    
    def __str__(self):
        return f"{self.club}, {self.league}, {self.year}"

class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_cart")
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.owner}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="in_cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="in_cart_item")
    quantity = models.IntegerField(default=1)
    price_total = models.FloatField(blank=True)

    def __str__(self):
        return f"{self.product} x{self.quantity} is in the cart"


