from django.shortcuts import render
from BusTime.models import *

def index(request):
    content = {
        'to_home': ToHome.getAll(),
        'to_station': ToStation.getAll(),
    }
    return render(request, "index.html", content)