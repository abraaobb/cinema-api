from rest_framework import serializers

from core import models


class ModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.ModelBase
        fields = "__all__"


class StudioSerializer(ModelSerializer):
    class Meta:
        model = models.Studio
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Movie
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["genre"] = instance.get_genre_display()
        representation["liked"] = instance.get_liked_display()
        representation["studio"] = instance.studio.name

        return representation


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["type"] = instance.get_type_display()
        return representation


class MoviePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoviePerson
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["movie"] = instance.movie.title
        representation["person"] = instance.person.name
        return representation
