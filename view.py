import cgi
import api_connection as apicon

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name = 'home')
def home_view(request):
    body = '<h1>Desafio Web 1.0</h1>'
    return Response(body)

@view_config(route_name = 'quotes')
def quotes(request):
    body = apicon.get_quotes()
    return Response(body)

@view_config(route_name = 'pick_quote')
def pick_quote(request):
    body = apicon.get_quote('%(name)s' % request.matchdict)
    return Response(body)

@view_config(route_name = 'random_quote')
