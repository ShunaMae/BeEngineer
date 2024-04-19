from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, TalkForm, UsernameChange, EmailChange
from .models import User, Talk
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth import logout

def index(request):
    return render(request, "main/index.html")

@login_required
def friends(request):
    friends = User.objects.exclude(id = request.user.id)
    context = {
        "friends": friends
    }
    print(friends)
    return render(request, "main/friends.html", context)

def signup(request):
    if request.method == "GET":
        form = SignUpForm()

    elif request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid:
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = auth.authenticate(
                username = username,
                password = password
            )

            if user:
                auth.login(request, user)
                print(user)
                print(password)
            
            return redirect('index')
        
    context = {
        "form": form
    }
    return render(request, "main/signup.html", context)

class LoginView(auth_views.LoginView):
    authentication_form = LoginForm
    template_name = "main/login.html"

@login_required
def settings(request):
    return render(request, 'main/settings.html')

@login_required
def talk_room(request, user_id):
    friend = get_object_or_404(User, id=user_id)

    talks = Talk.objects.filter(
        Q(sender=request.user, receiver=friend) 
        | Q(sender=friend, receiver=request.user)
    ).order_by("time")

    if request.method == "GET":
        form = TalkForm()
    elif request.method == "POST":
        form = TalkForm(request.POST)

        if form.is_valid():
            # to be correct, the form equals talkform
            new_talk = form.save(commit=False)
            new_talk.sender = request.user 
            new_talk.receiver = friend
            new_talk.save()
            return redirect("talk_room", user_id)

    context = {
        "friend": friend,
        "talks": talks,
        "form": form,
    }

    return render(request, "main/talk_room.html", context)


@login_required
def username_change(request):
    if request.method == "GET":
        form = UsernameChange(instance=request.user)
    elif request.method == "POST":
        form = UsernameChange(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("username_change_done")
    
    context= {
        "form": form,
    }
    
    return render(request, "main/username_change.html", context)

@login_required
def username_change_done(request):
    return render(request, "main/username_change_done.html")


@login_required
def email_change(request):
    if request.method == "GET":
        form = EmailChange(instance = request.user)
    elif request.method == "POST":
        form = EmailChange(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect("email_change_done")
    
    context = {
        "form": form,
    }

    return render(request, "main/email_change.html", context)

@login_required
def email_change_done(request):
    return render(request, "main/email_change_done.html")


class PasswordChangeView(auth_views.PasswordChangeView):
    """Django 組み込みパスワード変更ビュー

    template_name : 表示するテンプレート
    success_url : 処理が成功した時のリダイレクト先
    """

    template_name = "main/password_change.html"
    success_url = reverse_lazy('password_change_done')

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):

    template_name = "main/password_change_done.html"

#class LogoutView(auth_views.LogoutView):
    pass

def logout_request(request):
    logout(request)
    return render(request, "main/logout.html")
