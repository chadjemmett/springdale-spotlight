from django.shortcuts import render
from rest_framework import viewsets
from . models import Winner
from . serializers import WinnerSerializer

class WinnerViewSet(viewsets.ModelViewSet):
        queryset = Winner.objects.all()
        serializer_class = WinnerSerializer
