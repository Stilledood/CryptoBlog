from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Answer,Category
from .forms import PostFrom,CommentForm,CategoryForm
from django.views.generic import View
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator
from user.decorators import class_login_required,class_permission_required


class PostList(View):
    '''Class to construct a view for list of post objects'''

    model=Post
    template_name='blog/post_list.html'
    page_kwargs='page'
    paginated_by=2

    def get(self,request):

        post_list=self.model.objects.all().order_by('-date_added')
        paginator=Paginator(post_list,self.paginated_by)
        page_number=request.GET.get(self.page_kwargs)
        try:
            page=paginator.page(page_number)
        except PageNotAnInteger:
            page=paginator.page(1)
        except EmptyPage:
            page=paginator.page(paginator.num_pages)

        if page.has_previous():
            previous_page_url="?{pkw}={n}".format(pkw=self.page_kwargs,n=page.previous_page_number())
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
            'post_list':page
        }


        return render(request,self.template_name,context)




class PostDetails(View):
    '''Class to construct a view for details of each post object'''

    model=Post
    template_name='blog/post_details.html'



    def get(self,request,pk):
        post=get_object_or_404(self.model,pk=pk)
        form=CommentForm()
        return render(request,self.template_name,{'post':post,'form':form})

    def post(self,request,pk):
        post=get_object_or_404(self.model,pk=pk)
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.author=self.request.user
            comment.save()
            return redirect(post.get_absolute_url())
        else:
            form=CommentForm()
            return render(request,self.template_name,{'form':form})









@class_permission_required('blog.add_post')
class PostCreate(View):
    '''Class to create views for creating objects'''

    model=Post
    form_class=PostFrom
    template_name='blog/post_create.html'




    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class()})

    def post(self,request):
        bound_form=self.form_class(request.POST,request.FILES)
        if bound_form.is_valid():
            new_post=bound_form.save()

            return redirect(new_post.get_absolute_url())
        else:
            return render(request,self.template_name,{'form':bound_form})




class CategoryCreate(View):
    '''Class to create a view for category objects creation'''

    form_class=CategoryForm
    template_name='blog/create_category.html'

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class()})

    def post(self,request):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            bound_form.save()
            return redirect('post_list')
        else:
            return render(request,self.template_name,{'form':bound_form})



class CategoryDetails(View):
    '''Class to construct a view with all the post objects from a specific category'''

    model=Category
    template_name='blog/category_details.html'
    paginated_by=3
    page_kwargs='page'

    def get(self,request,slug):
        category=get_object_or_404(self.model,slug=slug)
        post_list=Post.objects.filter(category=category)

        paginator=Paginator(post_list,self.paginated_by)
        page_number=request.GET.get(self.page_kwargs)

        try:
            page=paginator.page(page_number)

        except PageNotAnInteger:
            page=paginator.page(1)

        except EmptyPage:
            page=paginator.page(paginator.num_pages)

        if page.has_previous():
            previous_page_url="?{pkw}={n}".format(pkw=self.page_kwargs,n=page.previous_page_number())
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
            'category':category,
            'post_list':page,
        }

        return render(request,self.template_name,context)




def search_results(request):
    model=Post
    template_name='blog/search_result.html'
    if request.method == 'POST':
        searched=request.POST['searched']
        if searched:
            post_list=Post.objects.filter(title__icontains=searched)
            return render(request,template_name,{'post_list':post_list})














