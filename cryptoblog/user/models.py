from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse


class Profile(models.Model):
    '''class to create profile objects vconected to user objects'''

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email_confirmed=models.BooleanField(default=False)
    name=models.CharField(max_length=64)
    username=models.CharField(max_length=64)
    about=models.TextField()
    facebook_profile=models.URLField(max_length=254)
    linkedin_profile=models.URLField(max_length=254)
    twitter_profile=models.URLField(max_length=254)


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('dj-auth:profile_details',kwargs={'username':self.username})

    def get_update_url(self):
        return reverse('dj-auth:profile_update',kwargs={'username':self.username})


@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()




