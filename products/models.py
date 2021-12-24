from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(_('Product name'), max_length=20)
    product_price = models.DecimalField(_('Product price'), max_digits=6, decimal_places=2, default=0)

    def url_dispatcher(self):
        return self.id

    def __str__(self):
        return self.product_name
