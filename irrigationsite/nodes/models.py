from django.db import models
from django.utils.timezone import now

# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200, blank=True)
    moisture = models.FloatField(default=0)
    battery = models.FloatField(default=0)
    panel = models.FloatField(default=0, verbose_name="Solar Panel")
    com_status = models.BooleanField(default=False, verbose_name = "Conected")
    last_up = models.DateTimeField(default=now,  verbose_name = "Last Update")
    latitude = models.FloatField(default=-13.489983)
    longitude = models.FloatField(default=-72.457463)
    tx_frec = models.IntegerField(default=60)
    tx_slot = models.IntegerField(default=5)
    rx_window = models.IntegerField(default=10)
    def __str__(self):
        return self.name

class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    moisture = models.FloatField(default=0)
    battery = models.FloatField(default=0)
    panel = models.FloatField(default=0)
    update = models.DateTimeField(default=now,  verbose_name = "Last Update")

class Valve(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200, blank=True)
    flow = models.FloatField(default=0)
    battery = models.FloatField(default=0)
    panel = models.FloatField(default=0, verbose_name="Solar Panel")
    com_status = models.BooleanField(default=False, verbose_name="Conected")
    valve_command = models.BooleanField(default=False, verbose_name="Open Action")
    valve_status = models.BooleanField(default=False, verbose_name="Open Status")
    tot_flow = models.FloatField(default=0)
    last_up = models.DateTimeField(default=now,  verbose_name = "Last Update")
    latitude = models.FloatField(default=-13.489983)
    longitude = models.FloatField(default=-72.457463)
    tx_frec = models.IntegerField(default=60)
    tx_slot = models.IntegerField(default=5)
    rx_window = models.IntegerField(default=10)
    def __str__(self):
        return self.name

class ValveData(models.Model):
    valve = models.ForeignKey(Valve, on_delete=models.CASCADE)
    flow = models.FloatField(default=0)
    battery = models.FloatField(default=0)
    panel = models.FloatField(default=0)
    valve_status = models.BooleanField(default=False, verbose_name="Open Status")
    update = models.DateTimeField(default=now,  verbose_name = "Last Update")

