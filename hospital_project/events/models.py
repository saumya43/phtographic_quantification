from django.db import models

# Create your models here.
class events(models.Model):
  eventName = models.CharField(max_length=255)
  organizer = models.CharField(max_length=255)
  note = models.CharField(max_length=500)