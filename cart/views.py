from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest, Http404
from django.contrib.auth.decorators import login_required

from .models import CartItem

from movies.models import Movie

@login_required
def cart(request):
    if request.method == 'GET':
        items = CartItem.objects.filter(user=request.user).order_by('added_at')
        return render(request, 'cart.html', {'items': items})
    return Http404()

@login_required
def cart_remove(request):
    cid = request.GET.get('cid')
    r_all = request.GET.get('all')
    if cid is None and r_all is None:
        return HttpResponseBadRequest()
    if r_all is not None:
        if r_all == 'true':
            for e in CartItem.objects.filter(user=request.user):
                e.delete()
            return HttpResponseRedirect('/cart/')

    CartItem.objects.filter(cid=cid).delete()
    return HttpResponseRedirect('/cart/')

@login_required
def cart_add(request):
    mid = request.GET.get('mid')
    if mid == None:
        return HttpResponseBadRequest()
    movie = Movie.objects.filter(mid=mid).first()
    CartItem.objects.create(user=request.user, movie=movie)
    return HttpResponseRedirect('/cart/')
