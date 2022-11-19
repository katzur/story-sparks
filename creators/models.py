from django.db import models


class Creator(models.Model):
    """
    Class for the creator model
    """

    name = models.CharField(max_length=256)
    job = models.CharField(max_length=256, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    photo_url = models.URLField(max_length=1024, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
