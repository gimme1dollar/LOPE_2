from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Meme, Detail
from .serializers import MemeSerializer, DetailSerializer


class MemeList(APIView):
    def get(self, request, format=None):
        memes = Meme.objects.all()
        serializer = MemeSerializer(memes, many=True)
        return Response(serializer.data)


class MemeDetails(APIView):
    def get(self, request, meme):
        details = Detail.objects.filter(meme=meme).order_by('id')
        serializer = DetailSerializer(details, many=True)
        return Response(serializer.data)

    def post(self, request, meme):
        detail = request.data
        detail['meme'] = meme
        serializer = DetailSerializer(data=detail)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, meme):
        details = Detail.objects.filter(meme=meme)
        details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
