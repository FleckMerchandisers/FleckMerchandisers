# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template import loader


# Create your views here.

from django.contrib.auth import logout

from .models import Item

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm, ItemCreationForm

from django.db.models import Q


def index(request):
    latest_item_list = Item.objects.order_by('-pub_date')[:5]
    template = loader.get_template('spareparts/HomePage.html')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    context = {
            'latest_item_list': latest_item_list,
            'form': form,
            }
    return HttpResponse(template.render(context, request))

def detail(request, item_id):
    if request.method == 'POST':
        form = ItemCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ItemCreationForm()
    context = {
            'item_id' : Item.objects.get(item_id)
            }
    template = loader.get_template('spareparts/detail.html')
    return HttpResponse(template.render(context, request))

def logout_view(request):
    logout(request)
    return index(request)

def login_view(request):
    context={}
    template = loader.get_template('spareparts/login.html')
    return HttpResponse(template.render(context, request))

def collection(request):
    template=loader.get_template('spareparts/Collection.html')
    #if request.method == 'POST':
    #    print(request.GET)
    #    text = request.GET.get('search_box', '')
    #    item_list = Item.objects.order_by('-pub_date')
    #    context={'search_terms' : text.split(),
    #             'search':False,
    #             'item_list':item_list}
    #    return HttpResponse(template.render(context,request))
    
    item_list = Item.objects.order_by('-pub_date')
    print(item_list)
    context={
            'item_list': item_list,
            'search' :True
            }
    return HttpResponse(template.render(context,request))


def contact(request):
    context={}
    template = loader.get_template('spareparts/Contact.html')
    return HttpResponse(template.render(context, request))

def cart(request):
    context={}
    template = loader.get_template('spareparts/Cart.html')
    return HttpResponse(template.render(context, request))

def about(request):
    context={}
    template = loader.get_template('spareparts/About.html')
    return HttpResponse(template.render(context, request))

def payment(request):
    context={}
    template = loader.get_template('spareparts/Payment.html')
    return HttpResponse(template.render(context, request))

def signin(request):
    context={}
    template = loader.get_template('spareparts/Signin.html')
    return HttpResponse(template.render(context, request))

def createItem(request):
    if request.method == 'POST':
        form = ItemCreationForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.photo = request.FILES.get('photo', None)
            new.owner = request.user
            new.save()
    else:
        form = ItemCreationForm()
    context={
            'form': form,
            }
    template = loader.get_template('spareparts/CreateItem.html')
    return HttpResponse(template.render(context, request))
