from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.db.models import Max
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from . models import Color
from . serializers import ColorSerializer

# Create your views here.
@csrf_exempt
def get_color(request):
    colors = Color.objects.all()
    serializer = ColorSerializer(colors, many=True)
    return JsonResponse(serializer.data, safe=False)


def choose_color(request):
    max_percent = Color.objects.aggregate(Max("percent"))
    top_color = Color.objects.filter(percent=max_percent["percent__max"])
    if top_color:
        top_color = top_color[0]
        top_color.chosen = top_color.chosen + 1
        # have to recalculate the percent here. I'll have to account for zero in either clicked or chosen fields
        top_color.save()
    else:
        HttpResponse("No Colors")

    serializer = ColorSerializer(top_color)
    return JsonResponse(serializer.data, safe=False)
    
