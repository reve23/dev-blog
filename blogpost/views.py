from django.shortcuts import render
from .models import Blog, Comment

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def blog_detail(request,pk):
    item = Blog.objects.get(id=pk)
    return render(request,'blog.html',{'blog':item})

def add_blog(request):
    return render(request,'add.html')