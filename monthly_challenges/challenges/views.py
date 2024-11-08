from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request): 

    return HttpResponse("Run 10 MILES everyday!!")

def february(request):

    return HttpResponse("DO 100 PUSHUPS EVERYDAY")