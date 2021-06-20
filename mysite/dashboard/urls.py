from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('menu/', views.menu_list, name="menu_list"),
    path('menu/add/', views.menu_create, name="menu_add"),
    path('menu/<int:pk>/edit', views.menu_edit, name="menu_edit"),
    path('menu/<int:pk>/delete/', views.menu_delete, name="menu_delete"),

    path('product/', views.product_list, name="product_list"),
    path('product/add/', views.product_create, name="product_add"),
    path('product/<int:pk>/edit', views.product_edit, name="product_edit"),
    path('product/<int:pk>/delete/', views.product_delete, name="product_delete"),

    path('blog/', views.blog_list, name="blog_list"),
    path('blog/add/', views.blog_create, name="blog_add"),
    path('blog/<int:pk>/edit', views.blog_edit, name="blog_edit"),
    path('blog/<int:pk>/delete/', views.blog_delete, name="blog_delete"),

    path('chef/', views.chef_list, name="chef_list"),
    path('chef/add/', views.chef_create, name="chef_add"),
    path('chef/<int:pk>/edit', views.chef_edit, name="chef_edit"),
    path('chef/<int:pk>/delete/', views.chef_delete, name="chef_delete"),

    path('order/', views.order_list, name="order_list"),
    path('contact/', views.contact_list, name="contact_list")
]
