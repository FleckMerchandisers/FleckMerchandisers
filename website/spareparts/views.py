# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, you're at the index")

def detail(request, item_id):
    return HttpResponse("You're looking at item %s." % item_id)
