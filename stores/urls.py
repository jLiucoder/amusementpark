from django.urls import path
from . import views

urlpatterns = [
    path('stores/', views.stores, name='stores'),
]