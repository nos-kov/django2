from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpResponse

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    context = {"phones": Phone.objects.all(),}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phones = Phone.objects.filter(slug__contains=slug)
    for phone in phones:
        context = {"phone": phone,}
    return render(request, template, context)

#test