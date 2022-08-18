from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def firstApp(request):
    return HttpResponse('hello cohort 11')