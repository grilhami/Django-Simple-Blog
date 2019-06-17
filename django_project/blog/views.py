from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Gilang",
        "title": "Blog Post 1",
        "content": "This is a content",
        "date_posted": "June 18, 2019"
    },
    {
        "author": "Gilang",
        "title": "Blog Post 2",
        "content": "Second content",
        "date_posted": "July 18, 2019"
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { "title": "About"})
