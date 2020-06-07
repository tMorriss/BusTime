from django.db import models

class ToHome(models.Model):
    datetime = models.DateField()
    company = models.CharField(max_length=10)

class ToStation(models.Model):
    datetime = models.DateField()
    company = models.CharField(max_length=10)
