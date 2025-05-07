from django.db import models

# Choices for interest type
INTEREST_TYPE_CHOICES = (
    ('simple', 'Simple'),
    ('compound', 'Compound'),
)

class Investment(models.Model):
    deposit = models.FloatField()
    interest_rate = models.FloatField()
    years = models.IntegerField()
    interest_type = models.CharField(max_length=100, choices=INTEREST_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Deposit: {self.deposit}"


class Bond(models.Model):
    present_value = models.FloatField()
    interest_rate = models.FloatField()
    months = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bond Value: {self.present_value}"
