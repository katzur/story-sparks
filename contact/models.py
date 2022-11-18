from django.db import models

# Create your models here.

CONTACT_CHOICES = {
    ('REQUEST', 'Submit a request'),
    ('CONTACT', 'Ask a question'),
}


class Contact(models.Model):
    """
    Contact Model
    """
    name = models.CharField(max_length=254)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, blank=True)
    contact_type = models.CharField(max_length=20, choices=CONTACT_CHOICES)
    description = models.TextField()
    contact_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
