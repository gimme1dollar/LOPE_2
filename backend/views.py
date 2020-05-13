from .models import Meme, Detail
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MemeSerializer, DetailSerializer


class MemeList(APIView):
    def get(self, request, format=None):
        queryset = Meme.objects.all()
        serializer = MemeSerializer(queryset, many=True)
        return Response(serializer.data)
