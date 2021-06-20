from django.shortcuts import render, redirect
from . import servise
from .models import *
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
cont = {
        "phone": "tel://1234567920",
        "address": "198 West 21th Street, Suite 721 New York NY 10016",
        "email": "mailto:info@yoursite.com",
        "website": "https://www.youtube.com/",
        "map": "https://www.google.ru/maps/@41.329482,69.254856,16.74z"
    }


var = [{
    "image1": '../static/fronted/images/bg_6.jpg',
    'image2': '../static/fronted/images/bg_4.jpg',
    'title': 'Perfect Ingredients',
    "desc": f"""Far far away, behind the word mountains, 
    far from the countries Vokalia and Consonantia,
     there live the blind texts. Separated they live 
    in Bookmarksgrove right at the coast of the 
    Semantics, a large language ocean."""
}]


def index(request):
    abouts = servise.get_about()
    blogs = servise.get_blog()
    chefs = servise.get_chef()
    menus = servise.get_menu()
    products = servise.get_product()
    ctx = {
        "hom": "active",
        "blogs": blogs,
        "chefs": chefs,
        "menu": menus,
        "var": var,
        "abouts": abouts,
        "products": products,
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
    p = Paginator(blogs, 2)
    page_num = request.GET.get('page', 1)
    total_pages = len(blogs)
    try:
        page = p.page(page_num)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(p.num_pages)

    ctx = {
        "bl": "active",
        "blogs": blogs,
        "page": page,
        "p": p,
        "page_num": page_num,
        "total_pages": total_pages,
        "page_number": page.number

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
            print("AAA")
            form.save()
            print("a")
            return redirect("index")
        else:
            print(form.errors)
    ctx = { 
        "con": "active",
        "form": form,
        "cont": cont,
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
    new = servise.get_blog_id(pk)
    blogs = servise.get_blog()
    comments = servise.get_comment()
    model = Commit()
    form = CommitForm(request.POST, instance=model)
    print(55)
    if request.POST:
        print(56)
        print(request.POST)
        if form.is_valid():
            form.save()

            return redirect("our")
        else:
            print(form.errors)
    ctx = {
        "new": new,
        "blogs": blogs,
        "form": form,
        "comments": comments,
    }
    return render(request, 'fronted/taste/blog-single.html', ctx)


def our(request):
    new = servise.get_our()
    blogs = servise.get_blog().order
    comments = servise.get_comment()
    model = Commit()
    form = CommitForm(request.POST, instance=model)
    print(55)
    if request.POST:
        print(56)
        print(request.POST)
        if form.is_valid():
            form.save()

            return redirect("our")
        else:
            print(form.errors)
    ctx = {
        "news": blogs,
        "blogs": blogs,
        "comments": comments,

    }
    return render(request, 'fronted/taste/our.html', ctx)


def search(request):
    news = []
    if request.GET and request.GET.get("search"):
        news = Menu.objects.filter(name__icontains=request.GET.get("search"))
    ctx = {
        "newss": news,
        "search_count": len(news),
        "search_text": request.GET.get("search")
    }
    return render(request, "fronted/taste/search.html", ctx)
