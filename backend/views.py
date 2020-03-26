from django.shortcuts import render
from .models import Meme
from rest_framework import viewsets, permissions
from .serializers import MemeSerializer


class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    permission_classes = [permissions.AllowAny]
