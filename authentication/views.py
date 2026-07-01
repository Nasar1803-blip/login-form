from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from authentication.models import Profile



def login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            total_users = User.objects.count()
            return render(request, "dashboard.html", {
        "total_users": total_users
    })
        else:
            return render(request, "index.html", {
                "error": "Invalid Username or Password"
            })

    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/')

    return render(request, 'register.html')


def logout_user(request):
    logout(request)
    return redirect('/')
@login_required(login_url='/')
def dashboard(request):
    total_users = User.objects.count()

    return render(request, "dashboard.html", {
        "total_users": total_users
    })
@login_required(login_url='/')
def profile(request):
    return render(request, "profile.html")

@login_required(login_url='/')
def edit_profile(request):

    profile = request.user.profile

    if request.method == "POST":
        print("=" * 50)
        print("POST RECEIVED")
        print(request.POST)
        print(request.FILES)
        print("=" * 50)

        request.user.username = request.POST.get("username")
        request.user.email = request.POST.get("email")

        if "image" in request.FILES:
            print("IMAGE FOUND")
            profile.image = request.FILES["image"]
        else:
            print("NO IMAGE FOUND")

        request.user.save()
        profile.save()

        print("Saved Image :", profile.image)

        return redirect("/dashboard/")

    return render(request, "edit_profile.html", {
        "profile": profile
    })