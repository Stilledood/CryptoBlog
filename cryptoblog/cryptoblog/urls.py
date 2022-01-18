"""cryptoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from blog import urls as blog_urls
from django.views.generic import RedirectView
from news import urls as news_urls
from user import urls as user_urls
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from django.contrib.flatpages import views
from blog.feeds import AtomPostFeed,RssPostFeed



sitenews=[
    re_path(r'^atom/$',AtomPostFeed(),name='posts_atom_feed'),
    re_path(r'^rss/$',RssPostFeed(),name='posts_rss_feed')
]


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',RedirectView.as_view(pattern_name='post_list',permanent=False)),
    re_path(r'^blog/',include(blog_urls)),
    re_path(r'^news/',include(news_urls)),
    re_path(r'^user/',include(user_urls,namespace='dj-auth')),
    re_path(r'about/',views.flatpage,{'url':'/about/'},name='about'),
    re_path(r'^sitenews/',include(sitenews)),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:


    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [re_path(r'^debug/', include(debug_toolbar.urls)), ] + urlpatterns

import mimetypes
mimetypes.add_type("application/javascript", ".js", True)
admin.site.site_header='CoinBlog Admin'


