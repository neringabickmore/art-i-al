from django.db import models

class About(models.Model):

    class Meta:
        verbose_name_plural = "About Section"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=800)
    img = models.ImageField(null=True, blank=True) 
    url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):

    class Meta:
        verbose_name_plural = "Social Media Icons"

    name = models.CharField(max_length=254)
    icon = models.CharField(max_length=50)
    url = models.URLField(max_length=1024, default= '', null=True, blank=True)
    on = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name