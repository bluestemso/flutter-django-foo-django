from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import database
from rest_framework import status

# Create your views here.

def myapp(request):
    return render(request, 'main.html', {'name': 'Flutter Frank'})

@api_view(['GET', 'POST'])
def getData(request):
    if request.method == 'GET':
        data = database.pokedex
        return Response(data)
    
    elif request.method == 'POST':
        data = request.data
        number = data.get('number')
        try:
            parsedNumber = int(number)
            response_data = {
                'pokemon': database.pokedex[parsedNumber],
                'status': 'success'
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except:
            response_data = {
                'message': 'empty',
                'status': 'success',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)