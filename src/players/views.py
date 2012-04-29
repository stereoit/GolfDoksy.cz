
from django.contrib.auth.forms import AuthenticationForm
def ajax_login(request):
    form = AuthenticationForm(request.POST)
    logged_in = False
    if request.is_ajax() and form.is_valid():
        login(request, user)
        logged_in = True
    return HttpResponse(simplejson.dumps({ 'logged_in' : logged_in}), mimetype='application/json')


