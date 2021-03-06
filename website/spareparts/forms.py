from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Item, ItemOffer


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class ItemCreationForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'item_type', 'price', 'photo', 'description')


class OfferItemForm(ModelForm):
    class Meta:
        model = ItemOffer
        fields = ('message',)
