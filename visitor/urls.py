from django.urls import path

from . import views

urlpatterns = [
    path('profile', views.VisitorView.as_view(), name='profiles'),
    path('membership', views.MemberViewCreate.as_view(), name='memberships'),
    path('group', views.GroupViewCreate.as_view(), name='groups'),
    path('delete_group', views.GroupViewDelete.as_view(), name='delete_group'),
    path('byebye_member', views.MemberViewDelete.as_view(), name='deactivate_memberships')
]
