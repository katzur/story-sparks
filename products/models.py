from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Class for the category model
    """

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Scent(models.Model):
    """
    Class for the scent model
    """

    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Class for the product model
    """

    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, blank=True, null=True)
    scent = models.ForeignKey(
        'Scent', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=256, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    details = models.TextField(blank=True, null=True)
    ingredients = models.CharField(max_length=512, blank=True, null=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
