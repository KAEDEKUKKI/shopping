from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST.get('email', '')
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('/login')
    return render(request, 'register.html', locals())
def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user.is_active:
            auth.login(request, user)
            return redirect('/')
    return render(request, 'login.html', locals())
def sign_out(request):
    auth.logout(request)
    return redirect('/')
