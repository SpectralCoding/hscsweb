from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template

def index(request):
    t = get_template('pages/cardviewer.html')
    html = t.render(Context({'card_name': 'Test Card'}))
    return HttpResponse(html)