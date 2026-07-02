from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core import filters, models, serializers


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]


class StudioViewSet(BaseViewSet):
    queryset = models.Studio.objects.all()
    serializer_class = serializers.StudioSerializer
    filterset_class = filters.StudioFilter


class MovieViewSet(BaseViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    filterset_class = filters.MovieFilter


class PersonViewSet(BaseViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    filterset_class = filters.PersonFilter


class MoviePersonViewSet(BaseViewSet):
    queryset = models.MoviePerson.objects.all()
    serializer_class = serializers.MoviePersonSerializer
    filterset_class = filters.MoviePersonFilter
