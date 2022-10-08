from django.contrib.sitemaps import Sitemap
from datetime import date
from .models import Post


class PostSitemap(Sitemap):
    '''Class to cobsturct a sitemap foe Post objects'''

    changefreq='never'
    priority=0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self,post):
        return post.date_added

    def location(self,post ):
        return '/blog/%s'% (post.pk)


    