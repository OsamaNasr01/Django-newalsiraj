from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, ('you logged in successfully'))
            return redirect('users_list')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('there was an error logging in'))
            return redirect('login')
    else:
        return render(request, 'members/login.html', {})
