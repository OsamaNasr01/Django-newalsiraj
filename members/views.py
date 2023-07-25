from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, AddCompanyForm
from django.contrib.auth.models import User
from .models import Company
from urllib.parse import unquote



def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, ('You Logged in Successfully'))
            return redirect('users')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('There Was An Error Logging in'))
            return redirect('login')
    else:
        return render(request, 'members/login.html', {})
    

    
def logout_user(request):
    logout(request)
    messages.success(request, ('You Logged Out!'))
    return redirect('users')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            errors = form.errors
            error_message = errors.as_text().split(':')[0]
            messages.error(request, ('There Was An Error Registering' + error_message))
            return render(request, 'members/register.html', {'form' : form, 'errors': errors})
    else:
        form = RegisterUserForm()
        return render(request, 'members/register.html', {'form' : form})



def home(request):
    return render(request, 'home.html', {})

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user':user}
    return render(request, 'members/user_profile.html', context)

def users(request):
    context = {'users': User.objects.all()}
    return render(request, 'members/users.html', context)



def add_company(request):
    if request.method == 'POST':
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            company.save()
            messages.success(request, ('The Company has been Added Successfully!'))
            return redirect('home')
        else:
            errors = form.errors
            error_message = errors.as_text().split(':')[0]
            messages.error(request, ('There Was An Error Registering' + error_message))
            return render(request, 'members/add_company.html', {'form' : form, 'errors': errors})
    else:
        form = AddCompanyForm()
        return render(request, 'members/add_company.html', {'form' : form})





def co_profile(request, slug):
    decoded_slug = unquote(slug)
    company = get_object_or_404(Company, slug=decoded_slug)
    context = {'company': company}
    return render(request, 'members/co_profile.html', context)
