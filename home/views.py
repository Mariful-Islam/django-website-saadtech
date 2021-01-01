from django.shortcuts import render, redirect, HttpResponse, Http404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
import os
from django.conf import settings

def home(request):
    return render(request, 'index.html')

def reg(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('reg')
            else:
                user = User.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                username=username,
                                                email=email,
                                                password=password1)
                user.save()
                messages.info(request, 'Your account is created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching !!!')
            return redirect('reg')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def service(request):
    return render(request, 'service.html')

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog': blog})

def book(request):
    context = {'files': Book.objects.all()}
    return render(request, 'books.html', context)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(), content_type="applicaation/adminupload")
            response['content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
            return response

    raise Http404

def profile(request):
    return render(request, 'profile.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
