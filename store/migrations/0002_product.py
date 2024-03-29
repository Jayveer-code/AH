# Generated by Django 5.0 on 2024-03-14 01:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(auto_created=True, blank=True, max_length=200, null=True, unique=True)),
                ('image', models.ImageField(default=None, max_length=300, null=True, upload_to='news/')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('PUBLISH', 'PUBLISH'), ('DRAFT', 'DRAFT')], default='PUBLISH', max_length=200)),
                ('categories', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='store.categories')),
                ('filter_price', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='store.filter_price')),
                ('subcategories', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='store.subcategories')),
            ],
        ),
    ]
