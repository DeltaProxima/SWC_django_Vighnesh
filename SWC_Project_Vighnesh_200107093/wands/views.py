from django.shortcuts import render

from django.http import HttpResponse

def wands(request):
    return render(request,'wands/wands.html')

def phoenix(request):
    return render(request,'wands/phoenix.html')
def thestral(request):
    return render(request,'wands/thestral.html')
def elder(request):
    return render(request,'wands/elder.html')