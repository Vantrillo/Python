from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Michael Lam',
        'title': 'Comment',
        'content': '1st',
        'date_posted': 'May 29, 2021'
    },
    {
        'author': 'test2 ',
        'title': 'Comment',
        'content': '2nd',
        'date_posted': 'March 30, 2021'
    }
]
def home(request):
    context = {'posts': posts}
    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html', {'title': 'About'})

