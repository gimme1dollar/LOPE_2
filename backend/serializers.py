from .models import MEME
from rest_framework import serializers


class MEMESerializer(serializers.ModelSerializer):
    class Meta:
        model = MEME
        fields = ['id', 'name', 'type', 'level', 'parent', 'state']
