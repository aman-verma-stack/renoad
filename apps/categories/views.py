from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.

def categories_view(request):
    template_name = 'categories/categories_list.html'
    main = {}
    main['title'] = 'Categories | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    context['categories'] = Categories.objects.all()

    return render(request, template_name, context)


def subCategories(request, slug):
    template_name = 'categories/sub_categories.html'
    category_id = Categories.objects.filter(slug=slug).first()
    data = SubCategory.objects.filter(live=True, category=category_id.id)
    if not data:
        return HttpResponseRedirect('/category/')

    main = {}
    main['title'] = 'Categories | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    context['data'] = data

    return render(request, template_name, context)



def categories_details(request, slug):
    template_name = 'categories/categories_list.html'
    main = {}
    main['title'] = 'Coming Soon | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    context['categories'] = Categories.objects.all()

    return render(request, template_name, context)