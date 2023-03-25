from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User, Product, Cart, CartItem



def index(request):
    shirts = Product.objects.all

    if request.method == "POST":
        print('hello')
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.filter(email=email.lower()).exists():
            username = User.objects.get(email=email.lower()).username
            user = authenticate(request, username=username, password=password)
        else:
            print('login failed')
            messages.info(request, "Invalid username or password")
            return render(request, "shop/index.html", {"shirts":shirts})
        
        # Check if authentication successful
        if user is not None:
            print('login')
            login(request, user)
            return render(request, "shop/index.html", {"shirts":shirts})
            
        else:
            print('login failed')
            messages.info(request, "Invalid username or password")
            return render(request, "shop/index.html", {"shirts":shirts})
        
    if request.method == "GET":
        return render(request, "shop/index.html", {"shirts":shirts})

def logouttheuser(request):
    logout(request)
    return HttpResponseRedirect("/shop")


"""

Make page to buy a particular shirt

Make filters along navbars to display different leagues/decades of shirt

Make a cart that displays as dropdown when user logs in

Add option to leave reviews

Make sure user can order a specific size

"""
