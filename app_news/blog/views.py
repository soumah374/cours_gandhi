from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Bonjour le monde")


def store(request):
    return HttpResponse("Bonsoir le monde")