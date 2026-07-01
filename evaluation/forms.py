from django import forms
from .models import Terms

class TermsForm(forms.ModelForm):
    class Meta:
        model = Terms
        fields = ['title', 'is_active']