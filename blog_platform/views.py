from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['uname']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # creates a user
        myuser = User.objects.create_user(username=username, password=pass1, email=email)
        myuser.first_name = first_name
        #print(myuser.first_name)
        myuser.last_name = last_name
        myuser.save()

        messages.success(request, "Your account has been created successfully...")

        # function Name = 'login'
        return redirect('index')

    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['uname']
        passwd = request.POST['passwd']
        
        # To authenticate (In-built)
        user = authenticate(username=username, password=passwd)
        if user is not None:
            login(request, user)
            first_name = user.first_name
            print(first_name)
            return render(request, "index.html", context={'fname': first_name})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('signin')

    return render(request, "login.html")

def signout(request):
    logout(request)
    messages.success(request, "You have successfully Logged Out")
    return redirect('index')