from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST.get('email', '')
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except:
            messages.warning(request, 'Account already exists')
            return redirect('/register')
        return redirect('/login')
    return render(request, 'register.html', locals())
def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                messages.success(request, 'Successful')
                return redirect('/')
            else:
                messages.warning(request, 'Inactive user')
        else:
            messages.error(request, 'Invalid username/password!')
    return render(request, 'login.html', locals())
def sign_out(request):
    auth.logout(request)
    return redirect('/')
