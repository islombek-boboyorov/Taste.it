from django import forms
from .models import *


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders()
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact()
        fields = "__all__"


class CommitForm(forms.ModelForm):
    class Meta:
        model = Commit()
        fields = "__all__"


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu()
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product()
        fields = "__all__"


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog()
        fields = "__all__"


class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef()
        fields = "__all__"
