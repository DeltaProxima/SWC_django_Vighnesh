from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request,'home/index.html')

def wands(request):
    return render(request,'home/wands.html')
def brooms(request):
    return render(request,'home/wands.html')