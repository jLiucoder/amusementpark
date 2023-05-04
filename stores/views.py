from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import JlsStores, JlsItems


@login_required(login_url='home')
def stores(request):
    # getting all the value of cart
    stores = JlsStores.objects.all()
    template = loader.get_template('stores.html')
    context = {
        'stores': stores,
    }
    return render(request, 'stores.html', context)
    # return HttpResponse(template.render(context, request))


# The store_items function retrieves the corresponding store from the database using the get_object_or_404 function
# and filters the JlsItems queryset to only include items with the selected store
@login_required(login_url='home')
def store_items(request, store_id):
    store = get_object_or_404(JlsStores, st_id=store_id)
    items = JlsItems.objects.filter(st=store)
    context = {'store': store, 'items': items}
    return render(request, 'store_items.html', context)

# @login_required(login_url='home')
# def items(request, pk):
#     store_id = JlsStores.objects.get(pk=pk).st_id
#     myItems = JlsItems.objects.filter(JlsItems.st == store_id)
#     return render(request, 'store_items.html', {'myItems': myItems})


# @login_required(login_url='home')
# def items(request):
#     myItems = JlsItems.objects.all()
#     # myItems = JlsItems.objects.get(id=it_id)
#     template = loader.get_template('store_items.html')
#     context = {
#         'myItems': myItems,
#     }
#     return HttpResponse(template.render(context, request))
# return render(request, "store_items.html", {'items': items})
