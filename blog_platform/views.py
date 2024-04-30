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
        # validations
        if len(username) > 10:
            messages.error(request, "username exceeds the length")
            return redirect('signup')

        elif not username.isalnum():
            messages.error(request, "User name must be Alpha-Numeric")
            return redirect('signup')
        
        elif User.objects.filter(email=email):
            messages.error(request, "This Email is already Registered...")
            return redirect('index')

        elif pass1 == pass2:
            # creates a user
            try:
                myuser = User.objects.create_user(username=username, password=pass1, email=email)
                myuser.first_name = first_name
                # print(myuser.first_name)
                myuser.last_name = last_name
                myuser.save()

                messages.success(request, "Your account has been created successfully...")

            except:
                messages.error(request, "Username already Exists, Please create new user name...")
                return redirect('index')
        else:
            messages.error(request, "Please make sure that you Enter same password While 'Re-Entering' ")
            return redirect('signup')

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
            first_name = user.first_name.title()
            print(first_name)
            return render(request, "index.html", context={'fname': first_name, 'username': username})
        else:
            messages.error(request, "Bad Credentials, Please try Again...")
            return redirect('index')

    return render(request, "login.html")

def signout(request):
    logout(request)
    messages.success(request, "You have successfully Logged Out")
    return redirect('index')

def createPost(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        print(title)

    return render(request, "createPost.html")