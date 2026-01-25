from django.shortcuts import render
from django.http.response import HttpResponseRedirect

from movies.models import Movie
from .models import Review

from .forms import ReviewForm

def review_add(request):
    err_dict = {'action': 'review (add)'}
    if request.method == 'GET':
        mid = request.GET.get('mid') 
        if mid is None:
            return render(request, 'error.html', err_dict | {'error': 'No movie id provided'})
        movie = Movie.objects.filter(mid=mid).first()
        form = ReviewForm(initial={'mid': movie.mid})
        return render(request, 'editor.html', {'movie': movie, 'form': form})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if not form.is_valid():
            return render(request, 'error.html', err_dict | {'error': 'Form is invalid'})
        movie = Movie.objects.filter(mid=form['mid'].value()).first()
        Review.objects.create(
            rating=form['rating'].value(),
            user=request.user,
            title=form['title'].value(),
            comment=form['comment'].value(),
            movie=movie,
            is_visible=True
        )
        return HttpResponseRedirect('/movies/')

def review_edit(request):
    err_dict = {'action': 'review (edit)'}
    if request.method == 'GET':
        rid = request.GET.get('rid') 
        if rid is None:
            return render(request, 'error.html', err_dict | {'error': 'No review id provided'})
        review = Review.objects.filter(rid=rid).first()
        form = ReviewForm(initial={
            'rating': review.rating,
            'title': review.title,
            'comment': review.comment,
            'rid': review.rid
        })
        return render(request, 'editor.html', {'movie': review.movie, 'form': form})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if not form.is_valid():
            return render(request, 'error.html', err_dict | {'error': 'Form is invalid'})
        review = Review.objects.filter(rid=form['rid'].value()).first()
        if review.user != request.user:
            return render(request, 'error.html', err_dict | {'error': 'Non-owner user tried to edit a review'})
        review.rating = form['rating'].value()
        review.title = form['title'].value()
        review.comment = form['comment'].value()
        review.save()
        return HttpResponseRedirect('/movies/')

def review_delete(request):
    err_dict = {'action': 'review (edit)'}
    if request.method == 'GET':
        rid = request.GET.get('rid') 
        if rid is None:
            return render(request, 'error.html', err_dict | {'error': 'No review id provided'})
        review = Review.objects.filter(rid=rid).first()
        if review.user != request.user:
            return render(request, 'error.html', err_dict | {'error': 'Non-owner user tried to delete a review'})
        review.delete()

    return HttpResponseRedirect('/movies/')


def review_report(request):
    err_dict = {'action': 'review (edit)'}
    if request.method == 'GET':
        rid = request.GET.get('rid') 
        if rid is None:
            return render(request, 'error.html', err_dict | {'error': 'No review id provided'})
        review = Review.objects.filter(rid=rid).first()
        if review.user == request.user:
            return render(request, 'error.html', err_dict | {'error': 'Owner user tried to report their review'})
        review.is_visible = False
        review.save()

    return HttpResponseRedirect('/movies/')
