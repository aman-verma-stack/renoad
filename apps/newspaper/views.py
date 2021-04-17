from django.shortcuts import render

# Create your views here.


def newspaper_details(request):
    template_name = 'newspaper/newspaper_details.html'
    context = dict()
    context['main'] = {
        'title' : 'Aaj Newspaper | RenoAD',
        'description' : ''
    }
    

    return render(request, template_name, context)
