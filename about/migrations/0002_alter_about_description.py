# Generated by Django 4.1.5 on 2023-01-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]