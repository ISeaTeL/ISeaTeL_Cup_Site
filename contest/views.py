from django.shortcuts import render

# Create your views here.

def contest(request):
    return render(request, "base.html")