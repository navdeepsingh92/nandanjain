from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader


from .models import slotAvailability
# Create your views here.

def showslot(request):
    context = {
        "first_name": "Anjaneyulu",
        "last_name": "Batta",
        "address": "Hyderabad, India"
    }
    avalSlots=slotAvailability.objects.values()
    context=list(avalSlots)   
    print(context[0])


    return render(request,'book/index.html',context)
