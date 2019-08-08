from django.shortcuts import render
from .models import Blog
# Create your views here.
def bloghome(request):
    blogs = Blog.objects
    return render(request,'blog/blog.html')


def addblog(request):
    return render(request, 'blog/addblog.html')
