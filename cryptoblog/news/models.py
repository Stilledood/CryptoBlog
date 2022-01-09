from django.db import models
from django.shortcuts import reverse


class News(models.Model):
    '''Class to create a model for news objects'''

    title=models.CharField(max_length=254)
    body=models.TextField()
    date_added=models.DateField(auto_now_add=True)
    link=models.URLField(max_length=255)


    class Meta:
        ordering=['-date_added']
        get_latest_by='date_added'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_details',kwargs={'pk':self.pk})

