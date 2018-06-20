from django.urls import path, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
        path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
        template_name="blog/blog.html")),
        path('<int:pk>', DetailView.as_view(model=Post, template_name='blog/post.html'))
]
