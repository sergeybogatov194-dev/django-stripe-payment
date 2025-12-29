from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=150)
    percentage = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} в размере {self.percentage}"

class Tax(models.Model):
    name = models.CharField(max_length=150)
    percentage = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} в размере {self.percentage}"