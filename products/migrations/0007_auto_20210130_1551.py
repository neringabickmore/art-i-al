# Generated by Django 3.1.5 on 2021-01-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210130_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ft_new',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ft_preview',
        ),
        migrations.AddField(
            model_name='image',
            name='show_in_new',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]