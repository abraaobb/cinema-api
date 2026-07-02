from django_filters import rest_framework as filters

from core import models


class FilterBase(filters.FilterSet):
    id = filters.NumberFilter(field_name="id", lookup_expr="exact")
    is_active = filters.BooleanFilter(field_name="is_active", lookup_expr="exact")
    created_at = filters.NumberFilter(field_name="created_at", lookup_expr="year")


class StudioFilter(FilterBase):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    cnpj = filters.CharFilter(field_name="cnpj", lookup_expr="exact")

    class Meta:
        model = models.Studio
        fields = ["name", "cnpj"]


class MovieFilter(FilterBase):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    release_date = filters.DateFilter(field_name="release_date", lookup_expr="exact")
    studio = filters.CharFilter(field_name="studio__name", lookup_expr="icontains")
    genre = filters.ChoiceFilter(
        field_name="genre", lookup_expr="exact", choices=models.Movie.Genres
    )
    liked = filters.ChoiceFilter(
        field_name="liked", lookup_expr="exact", choices=models.Movie.Liked
    )
    rating = filters.RangeFilter(field_name="rating", lookup_expr="range")

    class Meta:
        model = models.Movie
        fields = ["title", "release_date", "studio", "genre", "liked", "rating"]


class PersonFilter(FilterBase):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    birth_date = filters.DateFilter(field_name="birth_date", lookup_expr="exact")
    type = filters.ChoiceFilter(
        field_name="type", lookup_expr="exact", choices=models.Person.Types
    )

    class Meta:
        model = models.Person
        fields = ["name", "birth_date", "type"]


class MoviePersonFilter(FilterBase):
    movie = filters.CharFilter(field_name="movie__title", lookup_expr="icontains")
    person = filters.CharFilter(field_name="person__name", lookup_expr="icontains")

    class Meta:
        model = models.MoviePerson
        fields = ["movie", "person"]
