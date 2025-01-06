from django.shortcuts import render
from django.http import HttpResponse
from . models import Price, Item

# Create your views here.

def index(request):
    items = Item.objects.filter(found=False)
    return render(request, "shiren/index.html", {"items": items})


