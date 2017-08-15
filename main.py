'''
Main application:

    - Before running this program make sure to run db_creation.py first.
      In case you have already done it, you are good to go! :)

    - Install geruquote lib from geruquote folder.

    - Pyramid app is created:
        - routes are defined
        - views are called from views.py
        - server is kept running
'''

from wsgiref.simple_server import make_server
from pyramid.session import SignedCookieSessionFactory
from pyramid.config import Configurator

if __name__ == '__main__':
    print ('Defining routes...')
    cookie_session = SignedCookieSessionFactory('itsagoodshow')
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_route('quotes', '/quotes')
        config.add_route('pick_quote', '/quotes/{quote_number}')
        config.add_route('log', '/log')
        config.add_route('log_id', '/log/{log_id}')
        config.set_session_factory(cookie_session)
        config.scan('views')
        app = config.make_wsgi_app()
    print('Starting server')
    ip = '0.0.0.0'
    port = 1234
    server = make_server(ip, port, app)
    print('Listening on {}:{}'.format(ip, port))
    server.serve_forever()
