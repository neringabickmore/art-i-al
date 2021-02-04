# Generated by Django 3.1.5 on 2021-01-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210124_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='main_img',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='room_view',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='show_in_gallery',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]