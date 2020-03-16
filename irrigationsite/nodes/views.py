from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Sensor, Valve

def index(request):
    return HttpResponse("Hello, world. You're at the Nodes index.")

def sensors(request):
    data = serializers.serialize("json", Sensor.objects.all())
    return HttpResponse(data)

def valves(request):
    data = serializers.serialize("json", Valve.objects.all())
    return HttpResponse(data)
