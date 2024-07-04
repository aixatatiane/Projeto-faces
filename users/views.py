from django.shortcuts import render

def login_(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def logout_(request):
    return render(request, 'users/register.html')