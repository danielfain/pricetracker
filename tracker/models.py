from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    requested_price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    current_price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title