from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "homepage.html")
    # return HttpResponse("homepage")


def about(request):
    return render(request, "about.html")
    # return HttpResponse("about")

# The views in Django are the functions that take a web request and return a web response.
