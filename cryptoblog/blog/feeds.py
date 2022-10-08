from datetime import datetime
from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from django.utils.feedgenerator import Atom1Feed,Rss201rev2Feed
from .models import Post,Category
from django.shortcuts import get_object_or_404

class BasePostFeedMixin():
    '''Class used to retrieve all the attributes needed to construct a feed'''

    title='CoinBlog latest posts'
    link=reverse_lazy('post_list')
    description=subtitle=('See lates posts from CoinBlog')

    def items(self):
        return Post.objects.all()[:10]

    def item_title(self,post):
        return post.format_title()

    def item_description(self,post):
        return post.short_text()

    def item_link(self,post):
        return post.get_absolute_url()





class AtomPostFeed(BasePostFeedMixin,Feed):
    '''Class to construct a atom feed '''

    feed_type = Atom1Feed

class RssPostFeed(BasePostFeedMixin,Feed):
    '''Class to construct a Rss Feed'''

    feed_type = Rss201rev2Feed



class BaseCategoryFeedMixin():
    '''Class to used to retrieve all the information needed to construct a feed for Category objects'''

    def get_object(self,request,category_slug):
        return get_object_or_404(Category,slug__iexact=category_slug)

    def description(self,category):
        return "News about {title}".format(title=category.title)

    def items(self,category):
        return category.post_set.all()[:10]

    def item_title(self,post):
        return post.format_title()

    def item_description(self,post):
        return post.short_text()

    def item_link(self,post):
        return post.get_absolute_url()

    def subtitle(self,category):
        return self.description(category)

    def title(self,category):
        return category.title

    def link(self,category):
        return category.get_absolute_url()





class AtomCategoryFeed(BaseCategoryFeedMixin,Feed):
    feed_type = Atom1Feed

class RssCategoryFeed(BaseCategoryFeedMixin,Feed):
    feed_type = Rss201rev2Feed
