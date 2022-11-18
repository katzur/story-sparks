from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    This view shows and submits the contact form and shows the success/error
    messages.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request('You successfuly contacted us!'))
            return redirect(reverse('contact'))
        else:
            messages.error(request('Failed to send your message. Please ensure the form is valid.'))
    else:
        form = ContactForm()

    template = 'contact/contact.html/'

    context = {
        'form': form,
        'bag_details_not_required': True
    }

    return render(request, template, context)
