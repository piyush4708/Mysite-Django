from django.shortcuts import redirect, render
# from django.contrib.auth.forms import 
from .form import RegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!, your account has been successfully created')
            return redirect('myapp:index')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})