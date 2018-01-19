from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm


class LoginView(View):

    def get(self, request):
        context = {'form': LoginForm()}
        return render(request, "login_form.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("login_username")
            password = form.cleaned_data.get("login_password")
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user and authenticated_user.is_active:
                login(request, authenticated_user)
                return redirect("home_page")
            else:
                form.add_error(None, "Usuario incorrecto o inactivo")
        context = {'form': form}
        return render(request, "login_form.html", context)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("login_page")

