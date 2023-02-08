from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def hello(request):
    return HttpResponse("GeekTech")


def time(request):
    times = datetime.datetime.now()
    return HttpResponse(times)

def goodbye(request):
    return HttpResponse("Goodbye bye bye")