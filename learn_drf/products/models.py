from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return f'{float(self.price * 6):.2f}'

    def get_discount(self):
        return '111'
    def __str__(self):
        return self.title
