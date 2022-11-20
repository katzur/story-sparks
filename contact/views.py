from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """
    This view shows and submits the contact form and shows the success/error
    messages.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yoour message has been sent!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Failed to send your message. Try again!')
    else:
        form = ContactForm()

    template = 'contact/contact.html/'

    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


def shipping_returns(request):
    """View to return shipping and returns page"""
    return render(request, 'contact/shipping-returns.html')
