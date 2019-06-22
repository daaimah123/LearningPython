from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='aview')
def aview(request):
	return Response('One')
