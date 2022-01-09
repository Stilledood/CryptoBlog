from django.urls import re_path
from .views import PostList,PostDetails,PostCreate

urlpatterns=[
    re_path(r'^$',PostList.as_view(),name='post_list'),
    re_path(r'^(?P<pk>\d+)/$',PostDetails.as_view(),name='post_details'),
    re_path(r'^create/$',PostCreate.as_view(),name='post_create'),




]