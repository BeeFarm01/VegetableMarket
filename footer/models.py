from django.db import models

# Create your models here.
class Footer1(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 500)

class Footer2(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 500)
    location = models.CharField(max_length = 200)
    call = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)


