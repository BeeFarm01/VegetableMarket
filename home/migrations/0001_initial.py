# Generated by Django 4.1.5 on 2023-01-27 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('button', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/home/')),
            ],
        ),
    ]
