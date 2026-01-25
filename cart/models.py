from django.db import models
from django.contrib.auth import get_user_model

import uuid

from movies.models import Movie

User = get_user_model()

class CartItem(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    movie = models.ForeignKey(Movie, models.CASCADE)
    added_at = models.DateField(auto_now_add=True)
    cid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def price(self) -> float:
        return self.movie.price
