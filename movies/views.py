from django.shortcuts import render

from .models import Movie

def movies(request):
    movies = Movie.objects.all().order_by('title')
    return render(request, 'movies.html', {'movies': movies})
