from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def display1 (request):
    return HttpResponse("<h1>Esta es la vista 1 de la app1 </h1>")

def display2 (request):
    return HttpResponse("<h1>Esta es la vista 2 de la App1</h1><br><h1>Hice un salto de linea</h1>")
