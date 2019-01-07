# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.template import loader


# Create your views here.

from .models import Item

from django.http import HttpResponse

#def index(request):
#  return HttpResponse("Hello, you're at the index")

def index(request):
    latest_item_list = Item.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_item_list': latest_item_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, item_id):
    return HttpResponse("You're looking at item %s." % item_id)
