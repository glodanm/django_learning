from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

# menu = ["About site", "Add article", "Feedback", "Log in"]

menu = [{'title': "About site", 'url_name': "about"},
    {'title': "Add article", 'url_name': "add_page"},
    {'title': "Feedback", 'url_name': "contact"},
    {'title': "Log in", 'url_name': "login"}
]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Main page',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About my site'})


def add_page(request):
    return HttpResponse('Adding an article')


def contact(request):
    return HttpResponse('Feedback')


def login(request):
    return HttpResponse('Log in')
# def categories(request, cat_id):
#     if request.POST:
#         print(request.POST)
#     return HttpResponse(f"<h1>Categories, <p>{cat_id}</p></h1>")
#
#
# def archive(request, year):
#     if int(year) > 2020:
#         return redirect('home', permanent=False)
#     return HttpResponse(f"<h1>Archive by year</h1><p>{year}</p>")


def show_post(request, post_id):
    return HttpResponse(f"Post display with id = {post_id}")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Display by category',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    # return render(request, "<h1>Page not found ;-(</h1>", status=404)
    return HttpResponseNotFound("<h1>Page not found ;-(</h1>", status=404)
