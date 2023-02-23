from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import stripe
from API.models import Item
import json

stripe.api_key = "sk_test_51MaD9mJPwivnOuu4xfFPoZPocoUK6TKIDMa84I9A7dMP9afmjMzEOO641cfNPwZMBV1JoOrT9rBGzgAZnTwKogUo00QgNg47Ko"


def item(request, id):
    list = get_object_or_404(Item, pk=id)
    return render(request, 'item.html', {'list': list, 'id': id})


def buy(request, id):
    object = get_object_or_404(Item, pk=id)
    name = object.name
    price = object.price
    name_search = stripe.Product.search(query="name:'%s'" % name)
    if len(name_search) == 0:
        product = stripe.Product.create(
            name=name,
            description="Покупка товара",
        )
        price = stripe.Price.create(
            unit_amount=int(price),
            currency="usd",
            product=product['id'],
        )
    else:
        product = name_search['data'][0]
        price = stripe.Price.search(query="product:'%s'" % product['id'])
        price = price['data'][0]

    session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': price['id'],
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url="http://127.0.0.1:8000/item/%s/" % id,
    )
    return HttpResponse(json.dumps(session))
