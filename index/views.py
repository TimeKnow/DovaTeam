from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UserForm

class IndexView(generic.View):

    template_name = 'index.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login/')
        return render(request, self.template_name)


def loginUserView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        return render(request, 'loginPage.html', {'createAccount': False, 'hasError': True, 'error_message': "Invalid username or password"})
    else:
        return render(request, 'loginPage.html', {'createAccount': False})

def createUserView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

        return render(request, 'loginPage.html', {'createAccount': True, 'hasError': True, 'error_message': "Account registration failed"})
    else:
        return render(request, 'loginPage.html', {'createAccount': True})

def logoutUserView(request):
    logout(request)
    return redirect('/login/')