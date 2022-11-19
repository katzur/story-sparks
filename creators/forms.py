from django import forms
from .models import Creator


class CreatorForm(forms.ModelForm):
    """
    Class for the creator model form
    """

    class Meta:
        model = Creator
        exclude = ("photo_url",)

    def __init__(self, *args, **kwargs):
        """
        Set field classes
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"
            ] = "border border-dark rounded-0"
