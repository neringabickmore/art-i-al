from django import forms
# from .widgets import CustomClearableFileInput
from .models import Product, Category, Collection, ImagesFolder, Image


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    # image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # customise field to see name rather than ID
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'field-styling'


class CollectionForm(forms.ModelForm):

    class Meta: 
        model = Collection
        fields = ('name', 'friendly_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'name',
            'friendly_name': 'friendly_name'
        }
        
        self.fields['name'].widget.attrs['class'] = 'field-styling'
        self.fields['friendly_name'].widget.attrs['class'] = 'field-styling'


class ImagesFolderForm(forms.ModelForm):

    class Meta: 
        model = ImagesFolder
        fields = ('name', 'imgs')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        imgs = Image.objects.all()

        labels = {
            'name': 'Folder name',
            'imgs': 'Select images',
        }
        for field in self.fields:
            self.fields[field].label = labels[field]
        
        self.fields['name'].widget.attrs['data-toggle'] = 'tooltip'
        self.fields['name'].widget.attrs['data-placement'] = 'top'
        self.fields['name'].widget.attrs['title'] = 'No spaces or special characters, use _ for word separation'
        self.fields['imgs'].widget.attrs['data-toggle'] = 'tooltip'
        self.fields['imgs'].widget.attrs['data-placement'] = 'top'
        self.fields['imgs'].widget.attrs['title'] = 'To select multiple images +shift'
        self.fields['name'].widget.attrs['class'] = 'field-styling'
        for field in self.fields:
            self.fields[field].label = labels[field]
        
