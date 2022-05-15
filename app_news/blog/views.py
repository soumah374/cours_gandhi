from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'salutation': "Bonjour la classe"}
    return render(request,"index.html",context)

def salutation(request,nom,annee):
    context = {'nom': nom, 
               'annee': annee
              }
    return render(request,"index.html",context)


def store(request):
    return HttpResponse(request,"Bonsoir le monde")