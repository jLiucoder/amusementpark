from datetime import timezone, timedelta, date
from random import randint

from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import JlsVisitors, JlsMember
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class VisitorView(LoginRequiredMixin, TemplateView):
    template_name = 'visitor/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            current_user_id = self.request.user.id
            curruser = JlsVisitors.objects.filter(user_id=current_user_id).first()
            context['curr'] = self.request.user
            context['curruser'] = curruser
        return context


class MemberView(LoginRequiredMixin, TemplateView):
    template_name = 'visitor/membership.html'

    # if already have the membership, then skip to homepage
    def get(self, request, *args, **kwargs):
        visitor = JlsVisitors.objects.filter(user_id=self.request.user.id).first()
        if JlsMember.objects.get(v=visitor):
            return redirect('home')
        return super().get(request, *args, **kwargs)


    def post(self, request, **kwargs):
        current_user_id = self.request.user.id
        visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()

        mem_id = randint(10000, 99999)
        mem_sdate = date.today()
        mem_edate = mem_sdate + timedelta(days=365)
        member = JlsMember.objects.create(
            v=visitor,
            mem_id=mem_id,
            mem_sdate=mem_sdate,
            mem_edate=mem_edate,
        )
        member.save()
        return redirect('home')
