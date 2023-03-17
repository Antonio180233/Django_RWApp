from django.db import models

# Create your models here.
station_choices = [('stage1', '007'), ('stage2', '030'), ('stage3', '020'), ('stage4', '054'), ('stage5', '066'), ('stage6', '070')]

class Sensor(models.Model):
 
    sensor_data = models.CharField(max_length=60, unique='TRUE')
    sensor_station = models.CharField(max_length=20, choices=station_choices)


   
