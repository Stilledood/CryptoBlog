from django.urls import re_path
from .views import PostList,PostDetails,PostCreate,CategoryCreate,CategoryDetails,search_results

urlpatterns=[
    re_path(r'^$',PostList.as_view(),name='post_list'),
    re_path(r'^(?P<pk>\d+)/$',PostDetails.as_view(),name='post_details'),
    re_path(r'^create/$',PostCreate.as_view(),name='post_create'),
    re_path(r'categorycreate/$',CategoryCreate.as_view(),name='category_create'),
    re_path(r'^category/(?P<slug>[\w\-]+)/$',CategoryDetails.as_view(),name='category_details'),
    re_path(r'^search/$',search_results,name='search')




]