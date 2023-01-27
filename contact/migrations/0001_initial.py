# Generated by Django 4.1.5 on 2023-01-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
