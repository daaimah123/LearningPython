from pyramid.renderers import render_to_response

def myview(request):
    return render_to_response('myapp:template.pt', {'a': 1}, request=request)