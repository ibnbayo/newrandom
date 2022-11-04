from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from bio.models import Bio, Photo
from . serializers import BioSerializer, PhotoSerializer
from django.contrib.auth.models import User


@api_view(["GET"])
# @renderer_classes([JSONRenderer])
def pic_api_view(request):
    try:
        photo = Photo.objects.all()
    except Photo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","POST"])
def pics_api_list_view(request):
    if request.method == "GET":
        adverts = Photo.objects.all()
        serializer = PhotoSerializer(adverts, many = True)
        return Response(serializer.data)

