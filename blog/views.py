from django.shortcuts import render,redirect,Http404
from .models import Post,Comment,PostLikes
from .forms import CommentForm,PostForm

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def posts(request):
    posts=Post.objects.order_by('-date_added')
    context={'posts': posts,'user':request.user}
    return render(request, 'blog/posts.html', context)

def post(request, post_id):
    post=Post.objects.get(id=post_id)
    comments=post.comment_set.order_by('date_added')
    likes=PostLikes.objects.filter(post=post).count()
    liked=PostLikes.objects.filter(user=request.user, post=post).count()
    if liked>=1:
        liked=True
    else:
        liked=False
    print(liked)

    if request.method!='POST':
        form=CommentForm()
    else:
        form=CommentForm(data=request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.owner=request.user
            new_comment.save()
            return redirect('blog:post', post_id=post_id)
    
    context={'text':post.text,'post':post, 'form':form,'comments':comments,'likes':likes,'liked':liked}
    return render(request, "blog/post.html", context)

def new_post(request):
    if request.user.is_superuser:
        if request.method!='POST':
            form=PostForm()
        else:
            form=PostForm(data=request.POST)
            if form.is_valid():
                new_post=form.save()
                return redirect('blog:posts')
        context={'form': form}
        return render(request, 'blog/new_post.html', context)
    else:
        raise Http404()

def like_post(request, post_id):
    new_like, created=PostLikes.objects.get_or_create(user=request.user, post=Post.objects.get(id=post_id))
    return post(request, post_id)