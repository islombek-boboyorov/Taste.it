from django.shortcuts import render, redirect
from . import servise
from .models import *
from .forms import *


def index(request):
    ctx = {
        "hom": "active"
    }
    return render(request, 'fronted/taste/index.html', ctx)


def about(request):
    abouts = servise.get_about()
    ctx = {
        "abouts": abouts,
        "abo": "active",
    }
    return render(request, 'fronted/taste/about.html', ctx)


def blog(request):
    blogs = servise.get_blog()
    ctx = {
        "bl": "active",
        "blogs": blogs,
    }
    return render(request, 'fronted/taste/blog.html', ctx)


def chef(request):
    model = Orders()
    form = OrdersForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    chefs = servise.get_chef()
    ctx = {
        "chr": "active",
        "form": form,
        "chefs": chefs,
    }
    return render(request, 'fronted/taste/chef.html', ctx)


def contact(request):
    model = Contact()
    form = ContactForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            print(form.errors)
    ctx = { 
        "con": "active",
        "form": form
    }
    return render(request, 'fronted/taste/contact.html', ctx)


def menu(request):
    model = Orders()
    form = OrdersForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    menus = servise.get_menu()
    products = servise.get_product()
    ctx = {
        "menus": "active",
        "menu": menus,
        "form": form,
        "products": products,
    }
    return render(request, 'fronted/taste/menu.html', ctx)


def reservation(request):
    ctx = {
        "res": "active"
    }
    return render(request, 'fronted/taste/reservation.html', ctx)


def view(request, pk):
    authors = servise.get_author()
    new = servise.get_blog_id(pk)
    blogs = servise.get_blog()
    ctx = {
        "new": new,
        "blogs": blogs,
        "authors": authors
    }
    return render(request, 'fronted/taste/blog-single.html', ctx)


def our(request):
    new = servise.get_our()
    blogs = servise.get_blog()
    ctx = {
        "news": new,
        "blogs": blogs,
    }
    return render(request, 'fronted/taste/our.html', ctx)
