'''dojo/view.py
'''

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x)+int(y)+int(z))

def total(request, numbers):
    return HttpResponse(sum(map(lambda s: int(s or 0), numbers.split("/"))))
