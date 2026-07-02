from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from core import models


class MovieActions:

    def curtir(movie):
        movie.liked = models.Movie.Liked.YES
        movie.save()
        return Response({"message": f"Movie '{movie.title}' liked successfully."})

    def estatisticas():
        total_movies = models.Movie.objects.count()
        total_liked_movies = models.Movie.objects.filter(
            liked=models.Movie.Liked.YES
        ).count()
        total_unliked_movies = models.Movie.objects.filter(
            liked=models.Movie.Liked.NO
        ).count()
        total_not_liked_movies = models.Movie.objects.filter(liked__isnull=True).count()

        return Response(
            {
                "total_movies": total_movies,
                "total_liked_movies": total_liked_movies,
                "total_unliked_movies": total_unliked_movies,
                "total_not_liked_movies": total_not_liked_movies,
            }
        )
