from django.core.validators import MinValueValidator
from django.db import models
from django.core.exceptions import ValidationError
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



def validate_price(value):
    if value < 0:
        raise ValidationError("Цена не может быть отрицательной")
    if len(str(value).split('.')[1]) > 2:
        raise ValidationError("Цена может иметь не более 2 знаков после точки")

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[validate_price])
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
