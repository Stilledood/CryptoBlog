from django.shortcuts import render,get_object_or_404
from .models import News
from django.views.generic import View,DetailView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

class NewsList(View):
    model=News
    template_name='news/news_list.html'
    page_kwargs='page'
    paginated_by=5

    def get(self,request):
        news_list=self.model.objects.all()
        paginator=Paginator(self.page_kwargs,self.paginated_by)
        page_number=request.GET.get(self.page_kwargs)

        try:
            page=paginator.page(page_number)

        except PageNotAnInteger:
            page=paginator.page(1)

        except EmptyPage:
            page=paginator.page(paginator.num_pages)

        if page.has_previous():
            previous_page_url="?{pkw}={n}".format(pkw=self.page_kwargs,n=page.next_page_number())
        else:
            previous_page_url=None

        if page.has_next():
            next_page_url="?{pkw}={n}".format(pkw=self.page_kwargs,n=page.next_page_number())
        else:
            next_page_url=None

        context={
            'is_paginated':page.has_other_pages(),
            'previous_page_url':previous_page_url,
            'next_page_url':next_page_url,
            'paginator':paginator,
            'news_list':page,
        }

        return render(request,self.template_name,context)




class NewsDetails(View):
    '''Class to construct a view for details of news object'''

    model=News
    template_name='news/news_details.html'

    def get(self,request,pk):
        news=get_object_or_404(self.model,pk=pk)
        return render(request,self.template_name,{'news':news})


