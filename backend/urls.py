from django.urls import path
from . import views

urlpatterns = [
    path('meme', views.MemeList.as_view())
]
