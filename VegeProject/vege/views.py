from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required

#Django username:admin
#Django email:admin@admin.com
#Django admin Password:helloworld12

@login_required(login_url="/login/")
def receipes(request):
    
    if request.method == "POST":

        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_description')
        receipe_img = request.FILES.get('receipe_image')
    
        print(receipe_name)
        print(receipe_desc)
        print(receipe_img)

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_desc,
            receipe_image = receipe_img
        )
    
        return redirect('/receipes/')
    
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    
    context = {'receipes':queryset}

    
    return render(request, 'receipes.html', context)

def update_receipe(request,id):
    queryset = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_description')
        receipe_img = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_desc

        if receipe_img:
            queryset.receipe_image = receipe_img
        
        queryset.save() 
        return redirect('/receipes/')
    context = {'receipe':queryset}
    return render(request, 'update_receipes.html', context)

def delete_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')

# Note: Never keep the login page name as login because there is built in function named as login() to keep track of the seesion.
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist')
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/receipes/')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('/register/')

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully')
        return redirect('/login/')

    return render(request, 'register.html')