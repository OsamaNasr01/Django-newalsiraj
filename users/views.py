from django.shortcuts import render



def signup(request):
    return render(request, 'user/user_signup.html', {'osama': 'osama'})