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
    genre = filters.ChoiceFilter(field_name="genre", lookup_expr="exact", choices=models.Movie.Genres)

    class Meta:
        model = models.Movie
        fields = ["title", "release_date", "studio", "genre"]
