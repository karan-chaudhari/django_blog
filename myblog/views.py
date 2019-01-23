from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Contact, Post
import json

with open('config.json') as f:
    params = json.load(f)['params']

def home(request):
    posts_list = Post.objects.all()[::-1]
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'params':params, 'posts':posts}
    return render(request, 'home.html', context)

def about(request):
    context = {'params':params}
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        msg = request.POST["msg"]
        cont = Contact(name=name, email=email, phone=phone, msg=msg)
        cont.save()
        messages.success(request,"Your details has been submitted. We will give you response very soon. Thank you so much.")
        return redirect('/contact')
    context = {'params':params}
    return render(request, 'contact.html', context)    