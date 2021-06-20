from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from taste.servise import *
from taste.models import *
from taste.forms import *


def login_required_decorator(f):
    print("A")
    return login_required(f, login_url="login")


def dashboard_page(request):
    return render(request, 'dashboard/index.html')


def dashboard_login(request):
    if request.POST:
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect("login")



def menu_list(request):
    menus = get_menu()
    ctx = {
        "menus": menus,
    }
    return render(request, 'dashboard/menu/list.html', ctx)



def menu_create(request):
    model = Menu()
    form = MenuForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('menu_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/menu/form.html', ctx)


def menu_edit(request, pk):
    model = Menu.objects.get(id=pk)
    form = MenuForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("menu_list")
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/menu/form.html', ctx)



def menu_delete(request, pk):
    model = Menu.objects.get(id=pk)
    model.delete()
    return redirect("menu_list")


def product_list(request):
    products = get_product()
    ctx = {
        "products": products,
    }
    return render(request, 'dashboard/product/list.html', ctx)



def product_create(request):
    model = Product()
    form = ProductForm(request.POST, request.FILES, instance=model)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)



def product_edit(request, pk):
    model = Product.objects.get(id=pk)
    form = ProductForm(request.POST or None, request.FILES,  instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("product_list")
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)

def product_delete(request, pk):
    model = Product.objects.get(id=pk)
    model.delete()
    return redirect("product_list")

def blog_list(request):
    blogs = get_blog()
    ctx = {
        "blogs": blogs,
    }
    return render(request, 'dashboard/blog/list.html', ctx)


def blog_create(request):
    model = Blog()
    form = BlogForm(request.POST, request.FILES,  instance=model)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/blog/form.html', ctx)


def blog_edit(request, pk):
    model = Blog.objects.get(id=pk)
    form = BlogForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("blog_list")
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/blog/form.html', ctx)



def blog_delete(request, pk):
    model = Blog.objects.get(id=pk)
    model.delete()
    return redirect("blog_list")



def chef_list(request):
    chefs = get_chef()
    ctx = {
        "chefs": chefs,
    }
    return render(request, 'dashboard/chef/list.html', ctx)


def chef_create(request):
    model = Chef()
    form = ChefForm(request.POST, request.FILES,  instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('chef_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/chef/form.html', ctx)



def chef_edit(request, pk):
    model = Chef.objects.get(id=pk)
    form = ChefForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("chef_list")
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/chef/form.html', ctx)


def chef_delete(request, pk):
    model = Chef.objects.get(id=pk)
    model.delete()
    return redirect("chef_list")


def order_list(request):
    order = get_order()
    ctx = {
        "order": order
    }
    return render(request, 'dashboard/order/list.html', ctx)


def contact_list(request):
    contact = get_contact()
    ctx = {
        "contact": contact
    }
    return render(request, 'dashboard/contact/list.html', ctx)
