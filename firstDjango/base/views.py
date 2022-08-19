import http
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def erhan(request):
    return HttpResponse("app oluşturuldu.....")