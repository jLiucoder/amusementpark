from django.urls import path

from . import views

urlpatterns = [
    path('parking', views.ParkingViewCreate.as_view(), name='parking'),
    path('parking_deletion', views.ParkingViewDeleteAll.as_view(), name='delete_parking'),

]
