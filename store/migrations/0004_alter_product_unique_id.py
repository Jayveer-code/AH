# Generated by Django 5.0 on 2024-03-14 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unique_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]