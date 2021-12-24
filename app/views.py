import json
import requests
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from contact.models import FeedBack
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from firebase_admin import db


# Remember the code we copied from Firebase.
# This can be copied by clicking on the settings icon > project settings, then scroll down in your firebase dashboard

def index(request):
    return render(request, "index.html")


def service(request):
    return render(request, "service.html")


@login_required(login_url="/accounts/login")
def messages(request):
    url = "https://kassa-aparat-default-rtdb.firebaseio.com/orders.json"
    payload = json.dumps({
        # 'order': order,
        'id': 1,
        'order_day': "12 decabr",
        "number": 4

    })
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "d40f61e7-bac1-e66b-0415-1169251aa220"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    context = {

    }
    return render(request, "messages.html", context)


@login_required(login_url="/accounts/login")
def message_detail(request, id):
    feedback = FeedBack.objects.get(id=id)
    context = {"feedback": feedback, "check": "only_feedback"}
    return render(request, "messages.html", context)


def about(request):
    return render(request, "about.html")


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    form = NewUserForm()
    return render(request, "registration/register.html", context={"register_form": form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "registration/login.html", context={"login_form": form})


def logout_user(request):
    logout(request)
    return redirect("home")
