from datetime import timedelta, date
from random import randint
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import JlsVisitors, JlsMember, JlsGroup
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from visitor.forms import VisitorInfoForm


class VisitorView(LoginRequiredMixin, TemplateView):
    template_name = 'visitor/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            current_user_id = self.request.user.id
            curruser = JlsVisitors.objects.filter(user_id=current_user_id).first()
            context['curr'] = self.request.user
            context['curruser'] = curruser

            if curruser.v_type == 'M':
                member = JlsMember.objects.get(v=curruser)
                context['member'] = member

        return context


class MemberViewCreate(LoginRequiredMixin, TemplateView):
    template_name = 'visitor/membership.html'

    def post(self, request, **kwargs):
        current_user_id = self.request.user.id
        visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()
        visitor.v_type = 'M'
        visitor.save()
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
        visitor.refresh_from_db()
        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            curruser = JlsVisitors.objects.filter(user_id=self.request.user.id).first()
            context['curruser'] = curruser

        return context


class MemberViewDelete(LoginRequiredMixin, View):
    template_name = 'visitor/member_deactivate.html'
    success_url = reverse_lazy('memberships')

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        current_user_id = self.request.user.id
        visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()
        visitor.v_type = 'I'
        visitor.save()
        JlsMember.objects.all().delete()
        visitor.refresh_from_db()
        return redirect(self.success_url)

class GroupViewCreate(LoginRequiredMixin, CreateView):
    template_name = 'visitor/group.html'
    form_class = VisitorInfoForm

    # if success, then go to groups
    def get_success_url(self):
        return redirect('groups')

    def form_valid(self, form):
        # this is the current user
        current_user_id = self.request.user.id
        visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()
        visitor.v_group = 'Y'
        visitor.save()
        profile = form.save(commit=False)
        profile.save()

        if JlsGroup.objects.count() == 0:
            member = JlsGroup.objects.create(
                v=visitor,
                group_size=1
            )
            member.save()
        else:
            member = JlsGroup.objects.get(v=visitor)
            member.group_size += 1
            member.save()

        visitor.refresh_from_db()
        return redirect('groups')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            visitor = JlsVisitors.objects.filter(user_id=self.request.user.id).first()
            JlsGroup.objects.count()
            # if JlsGroup.objects.count() != 0:
            context["group"] = JlsGroup.objects.count()
            # else:
            #     context["group"] = 0
        return context


class GroupViewDelete(LoginRequiredMixin, View):
    template_name = 'visitor/group_deletion.html'
    model = JlsGroup
    success_url = reverse_lazy('groups')

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        current_user_id = self.request.user.id
        visitor = JlsVisitors.objects.filter(user_id=current_user_id).first()
        visitor.v_group = 'N'
        visitor.save()
        JlsGroup.objects.all().delete()
        visitor.refresh_from_db()
        return redirect(self.success_url)
