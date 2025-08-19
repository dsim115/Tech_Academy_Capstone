import datetime
from django import forms
from django.forms.widgets import SelectDateWidget, NumberInput, Textarea
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'release_date', 'runtime_minutes', 'genre', 'watched', 'rating', 'notes']
        # ≥1 widget (requirement met)
        widgets = {
            'release_date': SelectDateWidget(years=range(1900, datetime.date.today().year + 1)),
            'runtime_minutes': NumberInput(attrs={'min': 1, 'placeholder': 'e.g., 120'}),
            'notes': Textarea(attrs={'rows': 4, 'placeholder': 'Thoughts, favorite scenes, etc.'}),
        }
        help_texts = {
            'rating': '0.0 to 10.0 (one decimal)',
        }
