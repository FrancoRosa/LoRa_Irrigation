from django.contrib import admin

# Register your models here.
from .models import Sensor, SensorData, Valve, ValveData

admin.site.register(Sensor)
admin.site.register(SensorData)
admin.site.register(Valve)
admin.site.register(ValveData)