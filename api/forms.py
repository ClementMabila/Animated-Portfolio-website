# your_app/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}))
    subject = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter Your Message', 'rows': 10}))
