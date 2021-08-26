from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'uni_name': 'Independent University, Bangladesh(IUB)',
        'year': '1993',
        'type': 'Private University'
    }
]

def home(request):
    #return HttpResponse('<h1>SPM Home</h1>')

    context = {
        'posts': posts
    }
    return render(request, 'spm/home.html', context)

def about(request):
    return render(request, 'spm/about.html', {'title': 'About'})
