from django.urls import re_path,reverse_lazy,include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.contrib.auth.forms import AuthenticationForm

app_name='user'

password_urls=[
    re_path('^change/$',auth_views.PasswordChangeView.as_view(template_name='user/password_change.html',success_url=reverse_lazy('dj-auth:password_change_done')),name='password_change'),
    re_path(r'^change/done/$',auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'),name='password_change_done'),
]

urlpatterns=[
    re_path(r'^$',RedirectView.as_view(pattern_name='dj-auth:login',permanent=False)),
    re_path(r'^login/$',auth_views.LoginView.as_view(template_name='user/login.html',authentication_form=AuthenticationForm,success_url=reverse_lazy('post_list')),name='login'),
    re_path(r'^logout/$',auth_views.LogoutView.as_view(template_name='user/logout.html',extra_context={'form':AuthenticationForm}),name='logout'),
    re_path(r'^password/',include(password_urls))
]