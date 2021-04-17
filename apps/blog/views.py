from django.shortcuts import render
from apps.categories.models import Categories 
from .models import *

# Create your views here.


def coming_soon_view(request):
    template_name = 'other_pages/coming_soon.html'
    main = {}
    main['title'] = 'Coming Soon | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }

    return render(request, template_name, context)



def blog_main(request):
    template_name = 'blogs/blog_main.html'
    context = dict()
    context['main'] = {
        'title' : 'Blog | RenoAD',
        'description' : ''
    }
    context['blog'] = Blog.objects.filter(live=True)
    context['other_blog_type'] = Categories.objects.all()

    return render(request, template_name, context)



def blog_details(request, slug):
    template_name = 'blogs/blog_details.html'
    context = dict()
    context['main'] = {
        'title' : 'Blog Details | RenoAD',
        'description' : ''
    }
    context['blog_details'] = Blog.objects.filter(live=True, slug=slug)

    return render(request, template_name, context)
