from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def simple_view(request):
    """Простое API представление, которое возвращает 200 код и JSON ответ 'Okay'"""
    return Response({"message": "Okay"}, status=status.HTTP_200_OK)
