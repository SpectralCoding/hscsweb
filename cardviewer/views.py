import json
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from cardviewer.models import Cards, Games

def index(request):
    t = get_template('pages/cardviewer.html')
    html = t.render(Context())
    return HttpResponse(html)

def carddata(request, request_cardid):
    cardlist = Cards.objects.filter(cardid=request_cardid)
    return HttpResponse(json.dumps(dict(cardlist[0])))