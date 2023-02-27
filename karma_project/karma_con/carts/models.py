from django.db import models
from accounts.models import Customer
from store.models import Product, Variation

# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.name

    def __unicode__(self):
        return self.product

    def get_total_item_price(self):
        return self.product.price * self.quantity

