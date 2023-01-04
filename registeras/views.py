# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect


def register(request):
    return render(request,'RESGIST/index.html')