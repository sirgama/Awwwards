from django import forms
from .models import Site

CATEGORIES_1 = ['Ecommerce', 'Blog/Newspaper', 'Portfolio', 'Landing Page', 'Django App']

class NewSiteForm(forms.ModelForm):
    
    sitename =forms.CharField(widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Image Caption'}), required=True)
    url =forms.URLField(widget=forms.URLField(attrs={'class': 'Input', 'placeholder': 'Enter URL to the Website'}), required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Project description '}), required=True)
    category =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'Input', 'placeholder': 'Choose a category'}),choices=CATEGORIES_1, required=True)
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Country '}), required=True)
    technologies = forms.CharField(widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Technologies used | separate with comma '}), required=True)
    image = forms.ImageField(required=True)
    
    class Meta:
        model = Site
        fields = '__all__'