from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    description = models.TextField(verbose_name="Description")
    price = models.PositiveIntegerField(verbose_name="Price")

    def __str__(self):
        return self.name
