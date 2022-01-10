from django.contrib.auth import get_user,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .tokens import account_acctivation_token
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from .models import Profile




class DisableAccount(View):
    '''Class to disable a user account'''

    success_url=settings.LOGIN_REDIRECT_URL
    template_name='user/disable_account.html'

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def get(self,request):
        return TemplateResponse(request,self.template_name)

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def post(self,request):
        user=get_user(request)
        user.set_unusable_password()
        user.is_active=False
        user.save()
        logout(request)
        return redirect(self.success_url)


class SignUpView(View):
    '''Class to create a view for sign up process'''

    form_class=SignUpForm
    template_name='user/signup.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'form':self.form_class()})

    def post(self,request,*args,**kwargs):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            user=bound_form.save(commit=False)
            user.is_active=False
            user.save()
            Profile.objects.update_or_create(user=user,defaults={'username':user.get_username()})
            current_site=get_current_site(request)
            subject='Activate you CoinBlog account'
            message=render_to_string('user/account_activation_email.html',
                                     {
                                         'user':user,
                                         'domain':current_site.domain,
                                         'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                                         'token':account_acctivation_token.make_token(user)
                                     })
            user.email_user(subject,message)
            messages.success(request,'Please confirm your email to complete the registration process')
            return redirect('dj-auth:login')
        else:
            return render(request,self.template_name,{'form':bound_form})



class ActivateAccount(View):
    '''Class to activate account bassed on the email link'''

    def get(self,request,uidb64,token,*args,**kwargs):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except (TypeError,ValueError,OverflowError):
            user=None

        if (user != None and account_acctivation_token.check_token(user,token)):
            user.is_active=True
            user.profile.email_confirmed=True
            user.save()
            Profile.objects.update_or_create(user=user,defaults={''})
            return redirect('dj-auth:login')
        else:
            messages.warning(request,'Confirmation link is no longer valid')
            return redirect('dj-auth:signup')

