from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from creators.forms import CreatorForm
from .models import Creator


class Creators(generic.ListView):
    """
    A view to return the list of creators
    """

    model = Creator
    context_object_name = "creators"
    template_name = "creators/creators.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['on_profile_page'] = True
        return context


class AddCreator(
    UserPassesTestMixin, SuccessMessageMixin, generic.CreateView
):
    """
    A view to display the creators form.
    To add new creators. Restricted to superusers only.
    """

    model = Creator
    form_class = CreatorForm
    success_message = "Successfully added new creator!"
    success_url = reverse_lazy("creators")

    def test_func(self):
        """
        Check if the user is a superuser
        """
        return self.request.user.is_superuser

    def handle_no_permission(self):
        """
        If user is not a superuser, display a toast message
        """
        messages.error(
            self.request, "You need to be authorised to do that."
        )
        return redirect("home")

    def form_invalid(self, form):
        """
        Show toast error message if the form is invalid
        """
        messages.error(
            self.request,
            "Whops, something went wrong! Please double-check the form.",
        )
        return super().form_invalid(form)


class UpdateCreator(
    UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView
):
    """
    A view to display the creator form.
    To update creators. Restricted to superusers only.
    """

    model = Creator
    form_class = CreatorForm
    success_message = "Successfully updated creator!"
    success_url = reverse_lazy("creators")

    def test_func(self):
        """
        Check if the user is a superuser
        """
        return self.request.user.is_superuser

    def handle_no_permission(self):
        """
        If user is not a superuser, display a toast message
        """
        messages.error(
            self.request, "You need to be authorised to do that."
        )
        return redirect("home")

    def form_invalid(self, form):
        """
        Show toast error message if the form is invalid
        """
        messages.error(
            self.request,
            "Oops, something went wrong! Please double-check the form.",
        )
        return super().form_invalid(form)


class DeleteCreator(
    UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView
):
    """
    A view to delete creators.
    Restricted to superusers only.
    """

    model = Creator
    template = "creators/creators.html"
    success_message = "Successfully deleted creator!"
    success_url = reverse_lazy("creators")

    def test_func(self):
        """
        Check if the user is a superuser
        """
        return self.request.user.is_superuser

    def handle_no_permission(self):
        """
        If user is not a superuser, display a toast message
        """
        messages.error(
            self.request, "You need to be authorised to do that."
        )
        return redirect("home")
