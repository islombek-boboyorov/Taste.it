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
