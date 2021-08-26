from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>SPM Home</h1>')

def about(request):
    return HttpResponse('<h1>About SPM</h1>')
