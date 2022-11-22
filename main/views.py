from django.http import HttpResponse
from django.shortcuts import render

from main.models import Post


def test_view(request):
    return HttpResponse('Всем привет, это Джанго!!')


def posts(request):
    posts_list = Post.objects.all()
    return render(request, 'main/posts.html', context={'posts': posts_list})
