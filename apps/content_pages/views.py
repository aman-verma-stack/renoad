from django.shortcuts import render
from .content import *

from .models import *
# Create your views here.


def about_view(request):
    template_name = 'homepage/about.html'
    main = {}
    main['title'] = 'About | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    context['about'] = About.objects.all()

    return render(request, template_name, context)


def cancellation_view(request):
    template_name = 'other_pages/cancelation.html'
    main = {}
    main['title'] = 'Cancellation Policy | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    context['cancellation'] = Cancellation.objects.all()

    return render(request, template_name, context)


def career_view(request):
    template_name = 'other_pages/career.html'
    main = {}
    main['title'] = 'Career | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    context['career'] = Career.objects.all()

    return render(request, template_name, context)


def e_paper_view(request):
    template_name = 'other_pages/e_paper.html'
    main = {}
    main['title'] = 'E-Papers | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    context['e_papers'] = Epapers.objects.all()

    return render(request, template_name, context)


def privacy_view(request):
    template_name = 'other_pages/privacy_policy.html'
    main = {}
    main['title'] = 'Privacy Policy | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    context['privacy'] = Privacy.objects.all()
    return render(request, template_name, context)


def terms_view(request):
    template_name = 'other_pages/term_conditions.html'
    main = {}
    main['title'] = 'Terms & Conditions | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    context['terms'] = Terms.objects.all()
    return render(request, template_name, context)


def feedback_view(request):
    template_name = 'other_pages/feedback.html'
    main = {}
    main['title'] = 'Feedback | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    context['feedback'] = Feedback.objects.all()
    return render(request, template_name, context)


def book_view(request):
    template_name = 'other_pages/how_to_book.html'
    main = {}
    main['title'] = 'How To Book | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    context['book'] = Book.objects.all()

    return render(request, template_name, context)


def quick_pay(request):
    template_name = 'homepage/quick_pay.html'
    main = {}
    main['title'] = 'Quick Payment | RenoAD'
    main['description'] = ''
    context = {
        'main': main,
    }
    return render(request, template_name, context)
