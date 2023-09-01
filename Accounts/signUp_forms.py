from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegister(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'focus:outline-cyan-200 focus:ring-2 focus:ring-cyan-600 focus:ring-offset-2', 'placeholder': "Write your username"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'focus:outline-cyan-200 focus:ring-2 focus:ring-cyan-600 focus:ring-offset-2', 'placeholder': "Write your first_name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'focus:outline-cyan-200 focus:ring-2 focus:ring-cyan-600 focus:ring-offset-2', 'placeholder': "Write your last_name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'focus:outline-cyan-200 focus:ring-2 focus:ring-cyan-600 focus:ring-offset-2', 'placeholder': "Write your email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'focus:outline-cyan-200 focus:ring-2 focus:ring-cyan-600 focus:ring-offset-2', 'placeholder': "Write your password"}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'focus:outline-cyan-200 focus:ring-2 focus:ring-cyan-600 focus:ring-offset-2', 'placeholder': "Write your confirm password"}), label='Confirm Password')

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        # Set help_text to an empty string for eachfield
        for field_name in self.fields:
            self.fields[field_name].help_text = ''
            
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
