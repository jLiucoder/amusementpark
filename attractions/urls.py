from django.urls import path
from . import views

urlpatterns = [
    path('attractions/', views.attractions, name='attractions'),
]