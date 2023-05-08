from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from django.utils import timezone

from datetime import datetime, date

from .models import JlsStores, JlsItems, JlsOrder
from visitor.models import JlsVisitors
from cart.models import JlsInvoi
from payment.models import JlsPay


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

    def post(self, request, *args, **kwargs):
        current_user_id = self.request.user.id
        visitor = JlsVisitors.objects.get(user_id=current_user_id)
        store_id = self.kwargs['store_id']
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))

        # Add the item to cart (order table)
        self.add_to_cart(visitor.v_id, store_id, item_id, quantity)

        return redirect(reverse('store_items', args=[store_id]))
    
    def add_to_cart(self, v_id, store_id, item_id, quantity):
        item = JlsItems.objects.get(pk=item_id)

        new_item = JlsOrder()
        new_item.order_date = timezone.now()
        new_item.order_quant = quantity
        new_item.it_id = item.it_id
        new_item.st_id = store_id
        new_item.v_id = v_id

        all_invoice = JlsInvoi.objects.all()
        in_st_today = all_invoice.filter(invoi_date=date.today(), invoi_type='Stores', jlsorder__v_id=v_id)
        print(len(in_st_today), date.today(), v_id==new_item.v_id)
        # if there's a invoice for the order today
        if len(in_st_today) != 0:
            print('here')
            invoi = in_st_today.first()
            # if this order has not been paid
            if JlsPay.objects.filter(invoi_id=invoi.invoi_id) != None:
                new_item.invoi_id = invoi.invoi_id
                invoi.invoi_amount += quantity*item.it_uprice
                invoi.save()
        else:
            # create a new invoice when there's no invoice
            temp = JlsInvoi.objects.create(
                invoi_date = date.today(),
                invoi_amount = quantity*item.it_uprice,
                invoi_type = 'Stores'
            )
            temp.save()
            new_item.invoi_id = temp.invoi_id
            new_item.save()

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
