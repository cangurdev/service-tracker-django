from django.db import models
from django.utils import timezone


class Record(models.Model):

    ownerName = models.CharField(max_length=30)
    ownerSurname = models.CharField(max_length=30)
    time = models.DateTimeField()
    description = models.TextField()
    address = models.TextField()
    phone = models.IntegerField()
    model = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    deviceType = models.CharField(max_length=30)
    status = models.CharField(max_length=255)
