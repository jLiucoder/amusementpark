from django.urls import path
from . import views

urlpatterns = [
    # path('cart/', views.cart, name='cart'),
    path('pay/', views.PaymentView.as_view(), name='pay'),
    path('paysuccess/', views.PaymentSuccess.as_view(), name='paysuccess'),
]
