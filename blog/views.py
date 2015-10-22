from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import User
from .models import Comment

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post(request, pk):
	post = Post.objects.get(pk=int(pk))
	comments = Comment.objects.filter(post=post).order_by('published_date')
	return render(request, 'blog/post.html', {'post': post, 'comments': comments})

def user_list(request):
	users = User.objects.all
	posts = Post.objects.all
	return render(request, 'blog/user_list.html', {'users': users, 'posts': posts})

def user_post_list(request, pk):
	user = User.objects.get(pk=int(pk))
	posts = Post.objects.filter(author=user).order_by('published_date')
	return render(request, 'blog/user_post_list.html', {'posts': posts})
