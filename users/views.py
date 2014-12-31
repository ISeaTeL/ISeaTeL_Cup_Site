from django.shortcuts import render, redirect
from users.forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def create(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'user.html', {'form': user_form})
    return render(request, 'user.html', {'form': UserCreationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        user_form = AuthenticationForm(data=request.POST)
        if user_form.is_valid():
            user = authenticate(username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password'])
            print user
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'user.html', {'form': user_form})
    return render(request, 'user.html', {'form': AuthenticationForm()})
