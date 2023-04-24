from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.VisitorListView.as_view())
]
