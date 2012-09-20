from django.forms import forms
from django.forms.fields import CharField, EmailField

__author__ = 'david'


class ContactForm(forms.Form):
    name = CharField()
    email = EmailField()
    message = CharField()