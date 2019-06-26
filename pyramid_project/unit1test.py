from pyramid.view import view_config

@view_config(renderer='myapp:template.pt')
def myview(request):
    return {'a':1}