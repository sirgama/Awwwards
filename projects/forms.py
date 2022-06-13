from cloudinary.forms import CloudinaryFileField
from django import forms
from .models import Site


CATEGORIES_1 = [
    ('Ecommerce', 'Ecommerce'),
    ('Portfolio', 'Portfolio'),
    ('DjangoApp', 'DjangoApp'),
    ('ArtsnCulture', 'ArtsnCulture'),
]

class NewSiteForm(forms.ModelForm):
    
    sitename =forms.CharField(widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Image Caption'}), required=True)
    url =forms.URLField( required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Project description '}), required=True)
    category =forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'Input', 'placeholder': 'Choose a category'}),choices=CATEGORIES_1, required=True)
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Country '}), required=True)
    technologies = forms.CharField(widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Technologies used | separate with comma '}), required=True)
    image = CloudinaryFileField()
    
    class Meta:
        model = Site
        fields = ['sitename', 'url', 'description', 'category', 'country', 'technologies', 'image']