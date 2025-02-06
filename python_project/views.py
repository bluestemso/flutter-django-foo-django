from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import database

# Create your views here.

def myapp(request):
    return render(request, 'main.html', {'name': 'Flutter Frank'})

@api_view(['GET', 'POST'])
def getData(request):
    data = database.pokedex
    return Response(data)