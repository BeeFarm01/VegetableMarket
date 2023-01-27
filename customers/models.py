from django.db import models

# Create your models here.
class CustomerTitle(models.Model):
    title = models.CharField(max_length = 200)

class CustomerList(models.Model):
    image = models.ImageField(upload_to= "media/about/")
    name = models.CharField(max_length = 200)
    occupation = models.CharField(max_length = 200)
    description = models.TextField(max_length = 500)