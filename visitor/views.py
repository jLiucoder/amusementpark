from django.http import request
from django.shortcuts import render
from .models import JlsVisitors
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# class VisitorView(TemplateView):
#     # tempUser = User.objects.get(User.get)
#     # user = JlsVisitors.objects.get(user_id=)
#     # Post.objects.filter(status=True).select_related('author')
#     template_name = 'visitor/profile.html'
#     extra_context = {'profile': User}
#

class VisitorView(LoginRequiredMixin, TemplateView):
    template_name = 'visitor/profile.html'
    # extra_context = {'profile': self.get_context_date()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            current_user_id = self.request.user.id
            curruser = JlsVisitors.objects.filter(user_id=current_user_id).first()
            context['curr'] = self.request.user
            context['curruser'] = curruser
        return context
