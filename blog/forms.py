from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['text','name']
        labels={'text':'Content','name':'Name'}
        widgets={'text':forms.Textarea(attrs={'cols':80}),'name':forms.Textarea(attrs={'cols':2})}

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':20,'rows':2})}