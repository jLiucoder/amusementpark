from django.http import HttpResponse
from django.template import loader
from .models import JlsInvoi

def cart(request):
  mycart = JlsInvoi.objects.all().values()
  template = loader.get_template('show.html')
  context = {
    'mycart': mycart,
  }
  return HttpResponse(template.render(context, request))