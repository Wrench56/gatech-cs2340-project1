from django.shortcuts import render

from reviews.models import Review
from .models import Movie

from .forms import SearchForm

def movies(request):
    movies = Movie.objects.all().order_by('title')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if not form.is_valid:
            return render(request, 'error.html', {'action': 'search (movies)', 'error': 'Invalid search form'})
        movies = movies.filter(title__icontains=form['search'].value().strip())
    else:
        form = SearchForm

    reviews = []
    for movie in movies:
        reviews.append(Review.objects.filter(movie=movie))
    return render(request, 'movies.html', {'movies': movies, 'reviews': reviews, 'user': request.user, 'form': form})
