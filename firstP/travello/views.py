from django.http import HttpResponse
from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1= Destination()
    dest1.name = 'Alaska'
    dest1.img='1.png'
    dest1.price = 999

    dest2= Destination()
    dest2.name = 'Dallas'
    dest2.img='2.png'
    dest2.price = 777

    dest3= Destination()
    dest3.name = 'TEXAS'
    dest3.img='3.png'
    dest3.price = 888

    dests= [dest1, dest2, dest3]



    return render(request, 'index.html', {'dests': dests } )




