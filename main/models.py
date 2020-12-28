from django.db import models

# Create your models here.
class Link(models.Model):
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    link = models.URLField(max_length=500)
    logo = models.ImageField()
    posted_on = models.DateField(auto_now=True)