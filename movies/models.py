from django.db import models
 
import uuid

class Person(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='people')

    def __str__(self) -> str:
        return f'{self.name}'

class Movie(models.Model):
    MOVIE_GENRE = (
        ('ACTION', 'Action'),
        ('DRAMA', 'Drama'),
        ('COMEDY', 'Comedy'),
        ('HORROR', 'Horror'),
    )

    title = models.CharField(max_length=255)
    date_released = models.DateField()
    date_added = models.DateField()
    genre = models.CharField(choices=MOVIE_GENRE)
    director = models.ForeignKey(Person, models.CASCADE, related_name='director')
    summary = models.CharField(max_length=8195)
    image = models.ImageField(upload_to='movies')
    actors = models.ManyToManyField(Person, related_name='actor')
    price = models.FloatField()
    mid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return f'{self.title} ({self.date_released.year}) by {self.director}'
