from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from .forms import User_Registrations
from Cart.models import Cart


def Register_View(request):
    # Handling user registration
    if request.method == "POST":
        form = User_Registrations(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Cart.objects.create(user=user)
            login(request, user)
            messages.success(request, f'{username} account created')
            return redirect('Store:home')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}:{form.error_messages[msg]}')

    # Registration form
    form = User_Registrations()
    context = {
        'form': form
    }
    return render(request, 'UserSystem/register.html', context)

def Login_View(request):
    # Handling user Login
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('Store:home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    # Login form
    form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'UserSystem/login.html', context)

@login_required
def Logout_View(request):
    logout(request)
    return redirect('/')