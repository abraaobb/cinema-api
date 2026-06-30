from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core import models, serializers


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]


class StudioViewSet(BaseViewSet):
    queryset = models.Studio.objects.all()
    serializer_class = serializers.StudioSerializer


class MovieViewSet(BaseViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class PersonViewSet(BaseViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class MoviePersonViewSet(BaseViewSet):
    queryset = models.MoviePerson.objects.all()
    serializer_class = serializers.MoviePersonSerializer
