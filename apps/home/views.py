from django.views.generic import *
from django.shortcuts import render
from django.http import HttpResponse

from .models import *


class IndexView(ListView):
    model = HomeContent
    context_object_name = 'data'
    template_name = 'homepage/index.html'

    def get_queryset(self):
        data = HomeContent.objects.prefetch_related('reviews_all').all()
        return data

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        data = context['data']
        context['main'] = {
            'title' : 'Reno Advertisement - Book Newspaper Advertisements At Genuine Cost.',
            'description' : 'Reno Advertisement - Book Newspaper Advertisements At Genuine Cost.'
        }
        context['patners'] = Partners.objects.all()

        return context


def ContactView(request):
    template_name = 'homepage/contact.html'
    main = {}
    main['title'] = 'Contact | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }

    return render(request, template_name, context)



# class AboutView(ListView):
#     model = ''
#     template_name = 'homepage/about.html'
#     def get_queryset(self):
#         return

#     def get_context_data(self, **kwargs):
#         context = super(CareerView, self).get_context_data(**kwargs)
#         context['main'] = {
#             'title' : 'Career | RenoAD',
#             'description' : ''
#         }

#         return context
