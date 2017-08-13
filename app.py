from wsgiref.simple_server import make_server
from pyramid.config import Configurator

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_route('quotes', '/quotes')
        config.add_route('pick_quote', '/quotes/{quote_number}')
        config.add_route('random_quote', '/quotes/random')
        config.scan('views')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 1234, app)
    server.serve_forever()
