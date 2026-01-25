from django.db import models

from django.contrib.auth import get_user_model

import uuid

from movies.models import Movie

User = get_user_model()

class Review(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=63)
    comment = models.CharField(max_length=65535)
    movie = models.ForeignKey(Movie, models.CASCADE)
    is_visible = models.BooleanField(editable=True)
    date_created = models.DateField(auto_now_add=True)
    rid = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return f'{self.rating} by {self.user.username} for {self.movie.title}'
