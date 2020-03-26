from django.shortcuts import render
from .models import MEME
from rest_framework import viewsets, permissions
from .serializers import MEMESerializer


class MEMEViewSet(viewsets.ModelViewSet):
    queryset = MEME.objects.all()
    serializer_class = MEMESerializer
    permission_classes = [permissions.AllowAny]
