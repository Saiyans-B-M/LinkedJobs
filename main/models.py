from django.db import models
from datetime import datetime, timedelta

#model manager here
class MyModelManager(models.Manager):
    def get_queryset(self):
        now = datetime.now()
        min_posted_on = now - timedelta(days=4)
        return super(MyModelManager, self).get_queryset().filter(posted_on__gt=min_posted_on)


# Create your models here.
class Link(models.Model):
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    link = models.URLField(max_length=500)
    logo = models.ImageField()
    posted_on = models.DateField(auto_now=True)
    objects = MyModelManager()

class Subscriber(models.Model):
    email = models.EmailField(max_length=255)