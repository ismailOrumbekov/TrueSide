from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# def login_page(request):
#     return render(request, "Pages/loginPage.html")

def registration_page(request):
    return render(request, "Pages/RegistrationPage.html")

from django.contrib.auth import authenticate, login

def login_page(request):
    print("entered")
    if request.method == 'POST':
        print("posteed")
        username = request.POST['username']
        password = request.POST['password']
        # Изменяем вызов authenticate на именованные параметры
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            return redirect('login')

    return render(request, "Pages/loginPage.html")

