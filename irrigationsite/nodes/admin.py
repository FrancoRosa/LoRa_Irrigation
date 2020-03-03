from django.contrib import admin

# Register your models here.
from .models import Sensor, SensorData, Valve, ValveData

class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'com_status', 
                    'moisture', 'battery', 
                    'panel', 'tx_frec', 'tx_slot')

class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('sensor', 
                    'moisture', 'battery', 
                    'panel', 'update')


class ValveAdmin(admin.ModelAdmin):
    list_display = ('name', 'com_status',
                    'valve_status', 'valve_command',
                    'flow', 'tot_flow', 'battery',
                    'panel', 'tx_frec', 'tx_slot')
    list_editable = ('valve_command', 'valve_command')

class ValveDataAdmin(admin.ModelAdmin):
    list_display = ('valve', 
                    'valve_status', 'flow', 
                    'battery', 
                    'panel', 'update')

admin.site.register(Sensor, SensorAdmin)
admin.site.register(SensorData, SensorDataAdmin)
admin.site.register(Valve, ValveAdmin)
admin.site.register(ValveData, ValveDataAdmin)