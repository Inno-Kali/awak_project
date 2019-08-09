from django.shortcuts import render, redirect,get_object_or_404
from .models import Blog

# Create your views here.
def bloghome(request):
    blogs = Blog.objects
    return render(request,'blog/blog.html', { 'blogs':blogs})


def addblog(request):
    return render(request, 'blog/addblog.html')

def detail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blogs':blogdetail })
