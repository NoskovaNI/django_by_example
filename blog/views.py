from django.shortcuts import render, get_object_or_404
from .models import Post

# The logic of your application goes here; each view receives an
# HTTP request, processes it, and returns a response.


# display list of posts
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})


# display detailed information of post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {"post": post})
