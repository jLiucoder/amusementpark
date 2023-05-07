from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from .models import JlsStores, JlsItems
from visitor.models import JlsVisitors
from cart.models import JlsInvoi


class StoreViewCreate(LoginRequiredMixin, CreateView):
    template_name = 'stores.html'

    def get_success_url(self):
        return redirect(self.template_name)

    def get_context_data(self):
        if self.request.user.is_authenticated:
            context = {
                'stores': JlsStores.objects.all(),
            }
            return context


class ItemViewCreate(LoginRequiredMixin, CreateView):
    template_name = 'store_items.html'
    model = JlsItems
    fields = ['it_id', 'it_name', 'it_link', 'it_des', 'it_uprice']

    def get_success_url(self):
        return reverse('store_items', args=[self.kwargs['store_id']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            store_id = self.kwargs['store_id']
            store = get_object_or_404(JlsStores, st_id=store_id)
            items = JlsItems.objects.filter(st=store)
            context = {
                'store': store,
                'items': items
            }
        return context

    # def form_valid(self, request, form):
    #     print('sljkdhfao;hurg')
    #     store_id = self.kwargs['store_id']
    #     store = get_object_or_404(JlsStores, st_id=store_id)
    #     selected_items = []
    # quantity_list = []
    # for s_items in self.request.POST.getlist('item_id'):
    #     selected_items.append(s_items)

    # items = JlsItems.objects.filter(st=store)
    # selected_items = self.request.POST.getlist('item_id')
    # quantity_list = form.cleaned_data['quantity']
    # print(selected_items)

    # for i, item_id in enumerate(selected_items):
    #     item = get_object_or_404(items, it_id=item_id)
    #     quantity = quantity_list[i]
    #     print('item id: ', item_id)
    #     print('item name: ', item)
    #     print('quantity: ', quantity)

    # return redirect(reverse('store_items', args=[store_id]))

    def post(self, request, *args, **kwargs):
        store_id = self.kwargs['store_id']

        item_id = request.POST.get('item_id')
        quantity = request.POST.get('quantity')
        print('item id: ', item_id)
        print('quantity: ', quantity)

        # Get the item object
        item = JlsItems.objects.get(pk=item_id)
        print(item.it_id, item.it_name, item.it_uprice)

        # Create a new cart item object
        # cart_item = JlsCartItems(item=item, quantity=quantity)
        # cart_item.save()

        return redirect(reverse('store_items', args=[store_id]))

# The store_items function retrieves the corresponding store from the database using the get_object_or_404 function
# and filters the JlsItems queryset to only include items with the selected store
# @login_required(login_url='home')
# def store_items(request, store_id):
#     store = get_object_or_404(JlsStores, st_id=store_id)
#     items = JlsItems.objects.filter(st=store)
#     context = {'store': store, 'items': items}
#     return render(request, 'store_items.html', context)

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
