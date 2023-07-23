from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib.humanize.templatetags.humanize import naturalday


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # form['slug'] = form['first_name']
        if form.is_valid():
            form.save()
            # Do something with the form data.
            return redirect('users_list')
    else:
        form = UserForm()
    # form = UserForm
    return render(request, 'user/user_signup.html', {'form': form})


def users_list(request):
    users = User.objects.all()
    return render(request, 'user/users_list.html', {'users': users})