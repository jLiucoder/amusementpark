from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.shows_view, name='shows'),
#        path('shows/', views.ShowsView.as_view(), name='shows'),
]