from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.db.models import Max
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from . models import Color
from . serializers import ColorSerializer

# Create your views here.



@api_view(['GET', 'PUT'])
def color_data(request):
    if request.method == "GET":
        max_percent = Color.objects.aggregate(Max("percent"))
        top_color = Color.objects.filter(percent=max_percent["percent__max"])
        if top_color:
            top_color = top_color[0]
            top_color.chosen = top_color.chosen + 1
            top_color.percent = top_color.clicked / top_color.chosen
            top_color.save()

        serializer = ColorSerializer(top_color)
        return JsonResponse(serializer.data, safe=False)
        serializer = ColorSerializer(top_color)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "PUT":
        color = Color.objects.get(pk=request.data.get("id"))
        color.chosen = color.chosen + 1
        color.clicked = color.clicked + 1
        color.percent = color.clicked / color.chosen
        color.save()
        serializer = ColorSerializer(color)
        return JsonResponse({"msg": "Color updated", "data": serializer.data})




