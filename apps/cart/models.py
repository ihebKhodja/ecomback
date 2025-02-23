from django.db import models
from apps.users.models import User
from apps.ecom_api.models import Product

class Cart(models.Model):
    user=models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    products=models.ManyToManyField(Product)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.total_price
  