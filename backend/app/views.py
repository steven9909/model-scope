from django.shortcuts import render


def home(request):
    context = {
        "title": "Home Directory",
        "message": "This is rendered using Django templates!",
    }
    return render(request, "home.html", context)
