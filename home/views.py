from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base.html')


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def services(request):
    return render(request, "services.html")


def Gul(request):
    return render(request, "Gul.html")


def Milk(request):
    return render(request, "Milk.html")


def Agree(request):
    return render(request, "Agree.html")


def about(request):
    return render(request, "about.html")
