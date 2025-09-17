from django.db import models
from django.contrib import admin
class Car(models.Model):
    brand = models.CharField()
    model = models.CharField()
    release_date = models.DateField()
    color = models.CharField()
    mileage = models.DecimalField(max_digits=10,decimal_places=2)
    

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand','model','release_date','color','mileage')



