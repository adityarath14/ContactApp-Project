from django import forms
from contacts.models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name', 'phone', 'email', 'notes', 'profile_picture']