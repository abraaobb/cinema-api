from rest_framework import serializers

from .models import Movie, MoviePerson, Person, Studio


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ["name", "cnpj"]


class MovieSerializer(serializers.ModelSerializer):
    studio_name = serializers.ReadOnlyField(source="studio.name")

    class Meta:
        model = Movie
        fields = ["title", "release_date", "genre", "studio_name"]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class MoviePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePerson
        fields = "__all__"
