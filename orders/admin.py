from django.contrib import admin

from orders.models import SalesOrder, Account
from products.models import Product

# Register your models here.
admin.site.register(SalesOrder)
admin.site.register(Product)
admin.site.register(Account)