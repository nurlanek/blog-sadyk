from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login (request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {
                "error": "username or password is yanlis"
            })

    return render(request, "account/login.html")

def register_request(request):

    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")
