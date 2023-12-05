# your_app/forms.py
from django import forms
from .models import Yacht

class YachtForm(forms.ModelForm):
    class Meta:
        model = Yacht
        fields = ['title', 'price', 'description', 'yachtPhoto']
