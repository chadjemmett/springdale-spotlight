from django.urls import path
from . import views

urlpatterns = [
        path("", views.get_color),
        path("get-color/", views.choose_color),
        ]
