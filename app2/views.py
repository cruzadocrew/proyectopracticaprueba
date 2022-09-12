from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display3 (request):
    return HttpResponse("<h1>View 1 app 2</h1>")

def display4 (request):
    return HttpResponse("<h1>View 2 app 2aaaaaaaaa </h1>")
