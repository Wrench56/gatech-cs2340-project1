from django.shortcuts import render

from .models import Movie

def movies(request):
    movies = Movie.objects.all().order_by('title')
    print(request.user)
    return render(request, 'movies.html', {'movies': movies, 'is_logged_in': (request.user != 'AnonymousUser')})
