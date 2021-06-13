from django.db import models


class About(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)


class Chef(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    degree = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Orders(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=120, blank=False, null=False)
    check_in = models.CharField(max_length=120, blank=False, null=False)
    time = models.CharField(max_length=120, blank=False, null=False)
    guest = models.CharField(max_length=120, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Menu(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False, default=0)
    description = models.TextField(blank=False, null=False)
    menu = models.ForeignKey(Menu, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    create_data = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    a_name = models.CharField(max_length=120, blank=False, null=False)
    a_age = models.PositiveIntegerField(blank=False, null=False, default=0)
    a_image = models.ImageField(upload_to='image/', blank=False, null=False)
    a_description = models.CharField(max_length=120, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=150, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Our(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
