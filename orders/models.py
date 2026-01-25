from django.db import models
from django.contrib.auth import get_user_model

import uuid

from movies.models import Movie

User = get_user_model()

class Order(models.Model):
    ORDER_STATUS = (
        ('SHIPPED', 'Shipped'),
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
    )
    
    status = models.CharField(choices=ORDER_STATUS, default='UNPAID')
    user = models.ForeignKey(User, models.CASCADE)
    date_bought = models.DateField(auto_now_add=True)
    time_bought = models.TimeField(auto_now_add=True)
    oid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    movie = models.ForeignKey(Movie, models.CASCADE)
    added_at = models.DateField()

    def price(self) -> float:
        return self.movie.price
