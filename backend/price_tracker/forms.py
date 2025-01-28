from django import forms
from .models import TrackedItem


class TrackedItemForm(forms.ModelForm):
    class Meta:
        model = TrackedItem
        fields = ["url"]
