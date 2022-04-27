from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def posts(request):
    posts=Post.objects.order_by('-date_added')
    context={'posts': posts}
    return render(request, 'blog/posts.html', context)

def post(request, post_id):
    post=Post.objects.get(id=post_id)
    comments=post.comment_set.order_by('date_added')

    if request.method!='POST':
        form=CommentForm()
    else:
        form=CommentForm(data=request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            return redirect('blog:post', post_id=post_id)
    
    context={'text':post.text,'post':post, 'form':form,'comments':comments}
    return render(request, "blog/post.html", context)