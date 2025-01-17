from django.urls import path
from . import views

urlpatterns = [
        path("color-data/", views.color_data),
        # path("update_color/<str:color_name>", views.choose_color),
        ]
