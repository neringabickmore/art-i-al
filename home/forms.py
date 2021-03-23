from django import forms
# from .widgets import CustomClearableFileInput
from .models import About


class AboutForm(forms.ModelForm):

    class Meta: 
        model = About
        fields = ('name', 'description', 'img', 'url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Name',
            'description': 'Description',
            'img': 'Image',
            'url': 'URL',
        }
        for field in self.fields:
            self.fields[field].label = labels[field]
        
        self.fields['name'].widget.attrs['class'] = 'field-styling'
        self.fields['description'].widget.attrs['class'] = 'field-styling'
        self.fields['img'].widget.attrs['class'] = 'field-styling'
        self.fields['url'].widget.attrs['class'] = 'field-styling'
