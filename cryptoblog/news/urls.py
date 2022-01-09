from django.urls import re_path
from .views import NewsList,NewsDetails

urlpatterns=[
    re_path(r'^$',NewsList.as_view(),name='news_list'),
    re_path(r'^(?P<pk>\d+)/$',NewsDetails.as_view(),name='news_details')
]
