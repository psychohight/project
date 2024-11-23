from django.contrib import admin
from store.models import Order, Product, Cart


# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
