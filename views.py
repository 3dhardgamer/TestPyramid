'''
View configuration:
    - This program requires geruquote lib to be installed.

    - Pyramid views are defined here for each kind of request:
        - /                      -> intial webpage writen 'Desafio Web 1.0'
        - /quotes                -> quotes display as bullet points
        - /quotes/{quote_number} -> quote number and its quote
        - /quotes/random         -> a random quote from quotes

    - Pyramid endpoint returning database
'''

import geruquote
import uuid
import random
import json
import datetime

from db_setup import *
from logging_request import *
from pyramid.response import Response
from pyramid.view import view_config


# init_session creates a new unique id for new sessions
def init_session(request):
    session = request.session
    try:
        session['id']
    except KeyError as e:
        session['id'] = uuid.uuid4().hex

    return session

# route view config for home webpage
@view_config(route_name = 'home')
def home_view(request):
    session = init_session(request)
    logging_request(session['id'], request.path)
    body = '<h1>Desafio Web 1.0</h1>'
    return Response(body)

# route view config for quotes webpage
@view_config(route_name = 'quotes')
def quotes(request):
    session = init_session(request)
    logging_request(session['id'], request.path)
    body = geruquote.get_quotes()['quotes']
    bodyhtml = '<ul>'
    for x in body:
        bodyhtml += '<li>{}</li>'.format(x)
    bodyhtml += '</ul>'
    return Response(bodyhtml)

# route view config for quote_number or randomic quote_number
# If the request is random, select a random quote,
# otherwise select the quote referred to the given number
@view_config(route_name = 'pick_quote')
def pick_quote(request):
    session = init_session(request)
    logging_request(session['id'], request.path)
    q = request.matchdict['quote_number']
    bodytempl = '<p>{}</p>'
    if q == 'random':
        body = geruquote.get_quotes()['quotes']
        index = random.randint(0, len(body) - 1)
        bodyhtml = bodytempl.format(str(index) + ' ' + body[index])
    else:
        body = geruquote.get_quote(q)['quote']
        bodyhtml = bodytempl.format(body)
    return Response(bodyhtml)


# Below are define the endpoint views
def encode(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    else:
        return obj

# whole database is shown
@view_config(route_name = 'log')
def log(request):
    s = request_session.select()
    rs = s.execute()
    jd = json.dumps([dict(r) for r in rs], indent = 4, sort_keys = True, default = encode)
    return Response(jd)

# only selected log_id is shown
@view_config(route_name = 'log_id')
def log_id(request):
    q = request.matchdict['log_id']
    s = request_session.select(request_session.c.request_id == q)
    rs = s.execute()
    jd = json.dumps([dict(r) for r in rs], indent = 4, sort_keys = True, default = encode)
    return Response(jd)
