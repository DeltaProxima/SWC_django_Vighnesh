from django.shortcuts import render

from django.http import HttpResponse

def brooms(request):
    return render(request,'brooms/brooms.html')

def nimbus(request):
    return render(request,'brooms/nimbus.html')
def normal(request):
    return render(request,'brooms/normal.html')
def firebolt(request):
    return render(request,'brooms/firebolt.html')