from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from . models import Winner
from . serializers import WinnerSerializer


@csrf_exempt
def winner_data(request):
    winner = Winner.objects.last()
    serializer = WinnerSerializer(winner)
    return JsonResponse(serializer.data, safe=False)
