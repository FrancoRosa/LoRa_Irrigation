from django.db import models

# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    moisture = models.FloatField()
    battery = models.FloatField()
    panel = models.FloatField()
    com_status = models.BooleanField()
    last_up = models.DateTimeField
    latitude = models.FloatField()
    longitude = models.FloatField()
    tx_frec = models.IntegerField()
    tx_slot = models.IntegerField()
    rx_window = models.IntegerField()

class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    moisture = models.FloatField()
    battery = models.FloatField()
    panel = models.FloatField()
    update = models.DateTimeField()

class Valve(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    flow = models.FloatField()
    battery = models.FloatField()
    panel = models.FloatField()
    com_status = models.BooleanField()
    valve_status = models.BooleanField()
    tot_flow = models.FloatField()
    last_up = models.DateTimeField
    latitude = models.FloatField()
    longitude = models.FloatField()
    tx_frec = models.IntegerField()
    tx_slot = models.IntegerField()
    rx_window = models.IntegerField()

class ValveData(models.Model):
    valve = models.ForeignKey(Valve, on_delete=models.CASCADE)
    flow = models.FloatField()
    battery = models.FloatField()
    panel = models.FloatField()
    valve_status = models.BooleanField()
    update = models.DateTimeField()

