# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template import loader


# Create your views here.

from django.contrib.auth import logout

from .models import Item

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm

#def index(request):
#  return HttpResponse("Hello, you're at the index")

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
