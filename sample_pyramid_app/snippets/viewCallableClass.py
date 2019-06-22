from pyramid.response import Response
from pyramid.view import view_config

class AView(object):
    def __init__(self, request):
        self.request = request
    
    @view_config(route_name='view_one')
    def view_one(self):
	   return Response('One')

    @view_config(route_name='view_two')
    def view_two(self):
	   return Response('Two')
