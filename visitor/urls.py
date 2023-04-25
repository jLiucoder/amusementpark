from django.urls import path

from . import views

urlpatterns = [
    path('profile', views.VisitorView.as_view(), name='profiles')
]
