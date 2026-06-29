from rest_framework import viewsets

from core import models, serializers


class StudioViewSet(viewsets.ModelViewSet):
    queryset = models.Studio.objects.all()
    serializer_class = serializers.StudioSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class MoviePersonViewSet(viewsets.ModelViewSet):
    queryset = models.MoviePerson.objects.all()
    serializer_class = serializers.MoviePersonSerializer
