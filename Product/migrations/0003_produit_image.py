# Generated by Django 3.1.3 on 2022-01-29 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_produit'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
