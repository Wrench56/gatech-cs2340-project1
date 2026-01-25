from django.shortcuts import render

from reviews.models import Review
from .models import Movie

def movies(request):
    movies = Movie.objects.all().order_by('title')
    reviews = []
    for movie in movies:
        reviews.append(Review.objects.filter(movie=movie))
    print(request.user.is_authenticated)
    return render(request, 'movies.html', {'movies': movies, 'reviews': reviews, 'user': request.user})
