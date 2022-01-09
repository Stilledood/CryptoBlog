from django import forms
from .models import Post,Answer
from django.core.exceptions import ValidationError


class PostFrom(forms.ModelForm):
    '''Class to create a form for post objects'''

    class Meta:
        model=Post
        fields=['title','body','tag']

    def clean_title(self):
        title=self.cleaned_data['title'].lower()
        dissallowed=['create','edit','delete']
        if title in dissallowed:
            return ValidationError('post title can not be {title}'.format(title=title))
        return title


class CommentForm(forms.ModelForm):
    '''Class to create a form for answer objects'''

    def __init__(self,*args,**kwargs):
        super(CommentForm,self).__init__(*args,**kwargs)
        self.fields['body'].label=False

    class Meta:
        model=Answer
        fields=['body']





