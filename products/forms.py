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
            'name': 'Programmatic name',
            'friendly_name': 'Display name*'
        }
        for field in self.fields:
            self.fields[field].label = labels[field]
        
        self.fields['name'].widget.attrs['data-toggle'] = 'tooltip'
        self.fields['name'].widget.attrs['data-placement'] = 'top'
        self.fields['name'].widget.attrs['title'] = 'No spaces or special characters, use _ for word separation'        
        self.fields['name'].widget.attrs['class'] = 'field-styling'
        self.fields['friendly_name'].widget.attrs['class'] = 'field-styling'


class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ('name', 'img', 'url', 'main_img',
                'room_view', 'show_in_gallery',
                'show_in_new')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        labels = {
            'name': 'Artwork image name',
            'img': 'Upload image',
            'url': 'Image link', 
            'main_img': 'Is this the main image?',
            'room_view': 'Is this room-view image?',
            'show_in_gallery': 'Show this image in the "gallery" banner on home page?',
            'show_in_new': 'Show this image in the "new" banner on home page?',
        }
        for field in self.fields:
            self.fields[field].label = labels[field]
        self.fields['name'].widget.attrs['class'] = 'field-styling'
        self.fields['img'].widget.attrs['class'] = 'field-styling'
        self.fields['url'].widget.attrs['class'] = 'field-styling'
    

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
        
