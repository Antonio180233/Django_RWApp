from django.shortcuts import render
from .models import Sensor
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def add_sensor(request):
    if request.method=="POST":
        
        sensor_data = request.POST['sensor_data']
        sensor_station = request.POST['sensor_station']
        sensor = Sensor(sensor_data=sensor_data, sensor_station=sensor_station)
        sensor.save()
        messages.success(request, 'Sensor agregado con éxito.')
    else:
        pass

  
        
    return render(request, 'index.html')

    
