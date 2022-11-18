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
            messages.success(request, 'You successfuly contacted us!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Failed to send your message. Make sure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html/'

    context = {'form': form}

    return render(request, template, context)
