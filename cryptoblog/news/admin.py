from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    '''Class to construct custom views for news objects in admin panel'''

    list_display = ('title','body',)
    date_hierarchy = 'date_added'
    list_filter = ('date_added',)
    search_fields = ('title','body',)
    fieldsets = (
        (None,{
            'fields':('title','body',)
        }),
        ('Related',{
        'fields':('link',)
        }),
    )



