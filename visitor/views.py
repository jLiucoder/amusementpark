from django.shortcuts import render
from .models import JlsVisitors
from django.views.generic import ListView


class VisitorListView(ListView):
    model = JlsVisitors
    context_object_name = 'profiles'
    template_name = 'visitor/profile.html'
