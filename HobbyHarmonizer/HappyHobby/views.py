from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login, logout

def login_view(request):
    print('yay')
    return HttpResponse("login")

def login_action(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        print('login success')
        return HttpResponse("login success!")
    else:
        # Return an 'invalid login' error message.
        print('invalid login')
        return HttpResponse("invalid login silly!")

def logout_view(request):
    logout(request)
