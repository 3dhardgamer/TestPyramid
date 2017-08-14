import cgi
import api_connection as apicon
import random

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name = 'home')
def home_view(request):
    body = '<h1>Desafio Web 1.0</h1>'
    return Response(body)

@view_config(route_name = 'quotes')
def quotes(request):
    body = apicon.get_quotes()['quotes']
    bodyhtml = '<ul>'
    for x in body:
        bodyhtml += '<li>{}</li>'.format(x)
    bodyhtml += '</ul>'
    return Response(bodyhtml)

@view_config(route_name = 'pick_quote')
def pick_quote(request):
    q = request.matchdict['quote_number']
    bodytempl = '<ul><li>{}</li></ul>'
    if q == 'random':
        body = apicon.get_quotes()['quotes']
        index = random.randint(0, len(body) - 1)
        bodyhtml = bodytempl.format(body[index])
    else:
        body = apicon.get_quote(q)['quote']
        bodyhtml = bodytempl.format(body)
    return Response(bodyhtml)
