from wsgiref.simple_server import make_server
from pyramid.config import Configurator

if __name__ == '__main__':
    print ('Defining routes...')
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_route('quotes', '/quotes')
        config.add_route('pick_quote', '/quotes/{quote_number}')
        config.scan('views')
        app = config.make_wsgi_app()
    print('Starting server')
    ip = '0.0.0.0'
    port = 1234
    server = make_server(ip, port, app)
    print('Listening on {}:{}'.format(ip, port))
    server.serve_forever()
