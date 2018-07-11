# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib.messages import error

def index(request):
    context={
        'users': User.objects.all()
    }
    return render (request, "user_app/index.html", context)

def new(request):
    return render (request, "user_app/new.html")

def create(request):
    errors = User.objects.basic_validator(request.POST)
    print request.POST
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new/')
    else:
        User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email']
        )
        return redirect('/')

def show(request, id):
    context={
        'user':User.objects.get(id=id)
    }
    return render (request, "user_app/show.html", context)

def edit(request, id):
    context={
        'user':User.objects.get(id=id)
    }
    return render (request, "user_app/edit.html", context)

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/edit/'+id)
    else:
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users/'+id)


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')
