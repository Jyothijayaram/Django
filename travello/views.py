from django.shortcuts import render
from .models import *

# Create your views here.
def indexTravello(request):
    dests=PlaceInfo.objects.all() # to extract data from the database into our web page
    

    
    return render(request,'indexTravello.html',{'dests':dests})











    