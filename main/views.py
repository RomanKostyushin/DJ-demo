from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from main.models import Post


def test_view(request):
    return HttpResponse('Всем привет, это Джанго!!')


def posts(request):
    posts_list = Post.objects.all()
    return render(request, 'main/posts.html', context={'posts': posts_list})


def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'main/post_details.html', context={'post': post})
