# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from datetime import datetime

import django.utils

class Item(models.Model):
  name = models.CharField(max_length=200)
  item_type = models.CharField(max_length=200)
  price = models.IntegerField(default=0)
  pub_date = models.DateTimeField(default=django.utils.timezone.now)

  def __str__(self):
    return self.name

  def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
