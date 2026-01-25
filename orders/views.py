from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import transaction

from functools import reduce

from cart.models import CartItem
from .models import Order, OrderItem

@login_required
def orders(request):
    if request.method != 'GET':
        return Http404()

    orders = Order.objects.filter(user=request.user)
    order_items = []
    for order in orders:
        order_items.append(OrderItem.objects.filter(order=order))

    return render(request, 'orders.html', {
        'orders': orders,
        'order_items': order_items
    })

@login_required
@transaction.atomic
def order_add(request):
    if request.method != 'GET':
        return Http404()

    cart_items = CartItem.objects.filter(user=request.user)
    if (len(cart_items) == 0):
        return render(request, 'error.html', {'action': 'order (add)', 'error': 'Cart is empty'})
    
    order = Order.objects.create(user=request.user, status='PAID')

    OrderItem.objects.bulk_create([
        OrderItem(
            order=order,
            movie=ci.movie,
            added_at=ci.added_at
        ) for ci in cart_items
    ])

    CartItem.objects.all().delete()

    return HttpResponseRedirect('/orders/')
