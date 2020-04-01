from .models import Meme, Detail
from rest_framework import serializers


class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ['id', 'name', 'type', 'level', 'parent', 'state']


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['id', 'meme', 'category', 'summary', 'description', 'remark']
