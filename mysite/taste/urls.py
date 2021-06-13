from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('menu/', views.menu, name="menu"),
    path('reservation/', views.reservation, name="reservation"),
    path('chef/', views.chef, name="chef"),
    path('view/<int:pk>/', views.view, name="view"),
    path('our/', views.our, name="our"),
]
