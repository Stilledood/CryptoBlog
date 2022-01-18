from django.contrib import admin
from .models import Post
from django.db.models import Count

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Class to allow us to configure the admin page for post objects'''

    list_display = ('title','date_added','tag_count','comments_count',)
    date_hierarchy = 'date_added'
    list_filter = ('date_added',)
    search_fields = ('title','body',)


    fieldsets = (
        (None,{
            'fields':('title','body','image',)
        }),
        ('Related',{
        'fields':('category','tag',)
        })
    )

    def get_queryset(self, request):
        queryset=super().get_queryset(request)
        return queryset.annotate(
            tag_number=Count('tag'),
            comments_number=Count('answer')
        )

    def tag_count(self,post):
        return post.tag_number
    tag_count.short_description='Number of Tags'

    def comments_count(self,post):
        return post.comments_number
    comments_count.short_description='Number of comments'
