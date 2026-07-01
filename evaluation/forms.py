from django import forms
from .models import Terms

class TermsForm(forms.ModelForm):
    class Meta:
        model = Terms
        fields = ['title', 'is_active']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-teal-600 focus:border-teal-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-teal-500 dark:focus:border-teal-500',
                    'placeholder': ''
                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800'
                }
            )
        }