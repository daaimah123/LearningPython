from wsgiref.simple_server import make_server 
from pyramid.config import Configurator
from pyramid.response import Response

def hello_user(request):
	return Response('hello %(name)s!' % request.matchdict)

if __name__ == '__main__':
	config = Configurator()
	config.add_route('hello', '/hello/{name}')
	config.add_view(hello_user, route_name='hello')
	app =config.make_wsgi_app()
	server = make_server('0.0.0.0', 8080, app)
	print('visit "http://0.0.0.0:8080/hello/user"\n"Hit Ctrl+C to Exit"\n')
	server.serve_forever()
