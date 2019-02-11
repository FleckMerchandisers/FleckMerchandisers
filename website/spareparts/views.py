# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template import loader


# Create your views here.

from django.contrib.auth import logout

from .models import Item, ItemOffer

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm, ItemCreationForm, OfferItemForm

from django.db.models import Q

from django.contrib.auth.models import User

from django.core.mail import send_mail

from django.conf import settings

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required


def index(request):
    latest_item_list = Item.objects.order_by('-pub_date')[:5]
    template = loader.get_template('spareparts/HomePage.html')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
            'Thanks for creating an account !',
            'Thank you for joining our community, you can now log in and start adding your spareparts for sell !',
            'Fleckmerchandisers@gmail.com',
            [form.cleaned_data['email']],
            fail_silently=False,)
            return redirect("/login/")
    else:
        form = SignUpForm()
    context = {
            'latest_item_list': latest_item_list,
            'form': form,
            }
    return HttpResponse(template.render(context, request))

def detail(request, item_id):
    template = loader.get_template('spareparts/Detail.html')
    if request.method == 'POST':
        form = OfferItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.sender = request.user
            f.item = Item.objects.get(pk=item_id)
            f.dest = Item.objects.get(pk=item_id).owner
            f.save()
    else :
        form = OfferItemForm()

    context = {
            'form': form,
            'item' : Item.objects.get(pk=item_id)
            }
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
    item_list = Item.objects.order_by('-pub_date')
    if request.method == 'GET' and request.GET != {}:
        text = request.GET.get('search_box', '')
        final_list=[]
        for i in item_list:
            for term in text.split():
                if i.name in term or term in i.name or term in i.description:
                    final_list.append(i)
        context={'search':False,
                 'item_list':final_list}
        return HttpResponse(template.render(context,request))
    
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


def account(request, user):
    item_list = Item.objects.order_by("-pub_date")
    final_list =[]
    account_user = User.objects.get(username=user)
    for i in item_list:
        if i.owner.username == user:
            final_list.append(i)
    if account_user == request.user:
        own = True
        messages = []
        for i in ItemOffer.objects.order_by('dest'):
            if i.dest == account_user:
                messages.append(i)
    else:
        own = False
        messages=[]
    context={
            'own':own,
            'incoming_messages':messages,
            'item_list':final_list,
            'account_user': account_user,
            }
    template = loader.get_template('spareparts/Account.html')
    return HttpResponse(template.render(context,request))
