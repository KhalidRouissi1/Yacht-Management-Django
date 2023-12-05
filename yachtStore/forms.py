from django import forms
from .models import Yacht

class YakhtForm(forms.ModelForm):
    class Meta:
        model = Yacht
        fields = ['title', 'description', 'price', 'yachtPhoto']  # Add 'yachtPhoto' field for the image

   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply Tailwind CSS classes to fields
        for field_name in  ['title', 'description', 'price', 'yachtPhoto'] :
            self.fields[field_name].widget.attrs.update({
                'class': 'block w-full rounded-md border border-gray-300 focus:border-purple-700 focus:outline-none focus:ring-1 focus:ring-purple-700 py-1 px-1.5 text-gray-500'
            })
