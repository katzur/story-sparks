"""
Profile Forms
"""
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """
    Submit contact form
    """
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'phone_number',
            'contact_type',
            'description',
        ]
