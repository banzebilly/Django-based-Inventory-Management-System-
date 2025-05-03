from django.db import models

class Shoe(models.Model):
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    product = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.product} ({self.code}) from {self.country}: Cost={self.cost}, Quantity={self.quantity}"
