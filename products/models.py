from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Collection(models.Model):

    class Meta:
        verbose_name_plural = "Collection Names"

    name = models.CharField(max_length=50, null=True, blank=False, unique=True)
    friendly_name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Product Categories"

    name = models.CharField(max_length=50, null=True, blank=False, unique=True)
    friendly_name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=False, on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=254, null=True, blank=False, unique=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=False)
    collection_name = models.ForeignKey(
        'Collection', null=True, blank=False, on_delete=models.SET_NULL)
    description = models.TextField(max_length=800, null=True, blank=False)
    author = models.CharField(max_length=254, null=True, blank=False)
    dimensions = models.CharField(
        max_length=70, null=True, blank=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    images_folder = models.ForeignKey(
        'ImagesFolder', null=True, blank=False, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254, null=True, blank=False)
    tag = models.ForeignKey(
        'Tag', null=True, blank=True, on_delete=models.SET_NULL)
    is_sold = models.BooleanField(default=False)

    sort = ('collections')

    def __str__(self):
        return self.name


class Tag(models.Model):

    class Meta:
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=50, null=True, blank=False)
    friendly_name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Image(models.Model):

    class Meta:
        verbose_name_plural = "Artwork Images"

    name = models.CharField(max_length=254, null=True, blank=False, unique=True)
    img = models.ImageField(null=True, blank=False)
    url = models.URLField(max_length=1024, null=True, blank=False)
    main_img = models.BooleanField(default=False)
    room_view= models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ImagesFolder(models.Model):

    class Meta:
        verbose_name_plural = "Images Folders"

    name = models.CharField(max_length=254, null=True, blank=False, unique=True)
    imgs = models.ManyToManyField('Image')

    def __str__(self):
        return self.name
