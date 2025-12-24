from django import forms
from .models import Book

# Regular form(Not linked with model)
class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,label='Your Name')
    email=forms.EmailField(label='Email Address')
    message=forms.CharField(widget=forms.Textarea,label='Message')

# Modelform Automatically generated from Book model
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','published_date','isbn']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
