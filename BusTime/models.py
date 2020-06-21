from django.db import models

class ToHome(models.Model):
    datetime = models.DateTimeField()
    company = models.CharField(max_length=10)

    def __str__(self):
        return self.datetime + "(" + company + ")"

    def getAll():
        return ToHome.objects.all()

class ToStation(models.Model):
    datetime = models.DateTimeField()
    company = models.CharField(max_length=10)
    
    def getAll():
        return ToHome.objects.all()

    def __str__(self):
        return self.datetime + "(" + company + ")"