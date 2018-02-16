from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from blogs.models import Blog
from users.forms import LoginForm, SignUpForm


class LoginView(View):

    def get(self, request):

        if request.user.is_authenticated:
            messages.info(request, 'You are already logged in.')
            return render(request, "login_message.html")
        else:
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
                redirect_to = request.GET.get("next", "home_page")
                return redirect(redirect_to)
            else:
                messages.error(request, "Usuario incorrecto o inactivo")
        context = {'form': form}
        return render(request, "login_form.html", context)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("login_page")


class SignUpView(View):

    def get(self, request):
        context = {'form': SignUpForm()}
        return render(request, "signup_form.html", context)


    def post(self, request):

        form = SignUpForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            first_name = cd.get("first_name")
            last_name = cd.get("last_name")
            username = cd.get("username")
            email = cd.get("email")
            password1 = cd.get("password1")
            password2 = cd.get("password2")
            blogtitle = cd.get("blogtitle")

            possible_blogs = Blog.objects.filter(blog_title=blogtitle)
            possible_email = User.objects.filter(email=email)

            if len(possible_email) > 0:
                form.add_error(None, 'This email is already in use')

            if len(possible_blogs) > 0:
                form.add_error(None, 'This blog title is already in use')

            if len(possible_blogs) == 0 and len(possible_email) == 0:
                new_user = User.objects.create_user(username, email, password1, first_name=first_name, last_name=last_name)
                new_blog = Blog.objects.create(blog_title=blogtitle, user=new_user)
                new_user.save()
                new_blog.save()
                form = SignUpForm()
                message = "¡Usuario creado con éxito!"
                messages.success(request, message)
                return redirect('login_page')

        context = {'form': form}
        return render(request, "signup_form.html", context)





