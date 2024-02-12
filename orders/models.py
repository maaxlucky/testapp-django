from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class Account(models.Model):
    account_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.account_name}"


# My models are here
# Model of orders in our shop
class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    buy_date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)






