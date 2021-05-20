from django.shortcuts import render

from django.http import HttpResponse

def books(request):
    return render(request,'books/books.html')
def transfig(request):
    return render(request,'books/transfig.html')
def dada(request):
    return render(request,'books/dada.html')
def potions(request):
    return render(request,'books/potions.html')

