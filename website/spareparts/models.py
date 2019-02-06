# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from datetime import datetime

from django.contrib.auth.models import User

import django.utils


TYPE_CHOICES = (
    ('Electronics', 'Electronics'),
    ('Computer', 'Computer'),
    ('Car', 'Car'),
    ('Other', 'Other')
)


class Item(models.Model):
  name = models.CharField(max_length=200)
  item_type = models.CharField(max_length=200, choices=TYPE_CHOICES, default='Other')
  price = models.PositiveIntegerField(default=0)
  pub_date = models.DateTimeField(default=django.utils.timezone.now)
  photo = models.ImageField(upload_to='images', default=None, null=True, blank=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  description = models.CharField(max_length=10000, default="")

  def __str__(self):
    return self.name

  def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
