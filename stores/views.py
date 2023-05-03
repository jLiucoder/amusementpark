from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import JlsStores


@login_required(login_url='home')
def stores(request):
    # getting all the value of cart
    myStores = JlsStores.objects.all().values()
    template = loader.get_template('stores.html')
    context = {
        'myStores': myStores,
    }
    return HttpResponse(template.render(context, request))
