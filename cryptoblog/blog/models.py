from django.db import models
from django.shortcuts import reverse
from taggit.managers import TaggableManager
from django.conf import settings


class Post(models.Model):
    '''Class to construc models for creating post objects'''

    title=models.CharField(max_length=500)
    body=models.TextField()
    date_added=models.DateField(auto_now_add=True)
    tag=TaggableManager()



    class Meta:
        ordering=('-date_added',)
        get_latest_by='date_added'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_details',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('post_update',kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('post_delete',kwargs={'pk':self.pk})

    def get_comment_url(self):
        return reverse('comment_create',kwargs={'pk':self.pk})




class Answer(models.Model):
    '''Class to construct models for creating answer objects'''

    body=models.TextField()

    date_added=models.DateField(auto_now_add=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    class Meta:
        ordering=('-date_added',)
        get_latest_by='date_added'

    def __str__(self):
        return self.body[:50]



    def get_delete_url(self):
        return reverse('answer_delete',kwargs={'pk1':self.post.pk,'pk2':self.pk})





