from django.conf import settings
from django.contrib.auth import get_user
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import View

def class_login_required(cls):
    '''Construct a custom login required decorator so we can decorate a class not a function'''

    if (not isinstance(cls,type) or not issubclass(cls,View)):
        raise ImproperlyConfigured('class-login-decorator must be applied to sub-classes of View class')

    decorator=method_decorator(login_required)
    cls.dispatch=decorator(cls.dispatch)
    return cls



def class_permission_required(permission):
    '''Construct a custom permission check decorator'''

    def decorator(cls):
        if (not isinstance(cls,type) or  not issubclass(cls,View)):
            raise ImproperlyConfigured('class_permission_decorator must be applied to subclass of View class')
        check_auth=method_decorator(login_required)
        check_perm=method_decorator(permission_required(permission,raise_exception=True))
        cls.dispatch=(check_auth(check_perm(cls.dispatch)))
        return cls
    return decorator
