from django.shortcuts import render
from .models import Meme, Detail
from rest_framework import viewsets, permissions
from .serializers import MemeSerializer, DetailSerializer


class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    permission_classes = [permissions.AllowAny]


class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    permission_classes = [permissions.AllowAny]
