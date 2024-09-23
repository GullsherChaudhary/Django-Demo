from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#take request and return orders
def say_hello(request):
    return HttpResponse('Hello World')
