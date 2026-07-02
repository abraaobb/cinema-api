from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from core import actions, filters, models, serializers


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

    @action(detail=True, methods=["post"], url_path="curtir")
    def curtir(self, request, pk=None):
        response = actions.MovieActions.curtir(self.get_object())
        return response

    @action(detail=False, methods=["get"], url_path="estatisticas")
    def estatisticas(self, request):
        response = actions.MovieActions.estatisticas()
        return response


class PersonViewSet(BaseViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    filterset_class = filters.PersonFilter


class MoviePersonViewSet(BaseViewSet):
    queryset = models.MoviePerson.objects.all()
    serializer_class = serializers.MoviePersonSerializer
    filterset_class = filters.MoviePersonFilter
