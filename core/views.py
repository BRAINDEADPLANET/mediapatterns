from django.shortcuts import render
from .models import Post
from django.db.models import Count


def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.annotate(num_comments=Count('postComment')).all()
    else:
        posts = Post.objects.filter(active=True)
    context = {
        'posts': posts
    }
    template = 'core/index.html'
    return render(request, template, context)


def post_detail(request, slug):
    post = Post.objects.annotate(num_comments=Count('postComment')).get(slug=slug)
    context = {
        'post': post
    }
    template = 'core/post_detail.html'
    return render(request, template, context)




