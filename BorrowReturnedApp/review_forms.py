from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']          
    widgets = {
        'text': forms.Textarea(attrs={'class': 'border p-2 rounded-md'})
    }
