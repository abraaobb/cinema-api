from django.core import validators
from django.db import models


# Create your models here.
class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Studio(ModelBase):
    name = models.CharField(max_length=255, unique=True, null=False)
    cnpj = models.CharField(max_length=14, unique=True, null=False)

    def __str__(self):
        return self.name


class Movie(ModelBase):
    class Genres(models.TextChoices):
        ACTION = "a", "Action"
        COMEDY = "c", "Comedy"
        DRAMA = "d", "Drama"
        HORROR = "h", "Horror"
        SCI_FI = "s", "Sci-Fi"

    class Liked(models.TextChoices):
        LOVE = "l", "Love"
        YES = "y", "Yes"
        NO = "n", "No"

    title = models.CharField(max_length=255, unique=True, null=False)
    release_date = models.DateField()
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, related_name="movies")
    genre = models.CharField(max_length=1, null=False, choices=Genres.choices)
    liked = models.CharField(max_length=1, null=True, choices=Liked.choices)
    rating = models.FloatField(
        null=True,
        validators=[validators.MinValueValidator(0), validators.MaxValueValidator(5)],
    )

    def __str__(self):
        return self.title


class Person(ModelBase):
    class Types(models.TextChoices):
        ACTOR = "a", "Actor"
        DIRECTOR = "d", "Director"
        PRODUCER = "p", "Producer"

    name = models.CharField(max_length=255, unique=True, null=False)
    birth_date = models.DateField()
    type = models.CharField(max_length=1, null=False, choices=Types.choices)

    def __str__(self):
        return self.name


class MoviePerson(ModelBase):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="movie_people"
    )
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="person_movies"
    )

    def __str__(self):
        return f"{self.person.name} - {self.movie.title}"
