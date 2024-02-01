from django.contrib.auth import login
from django.db import IntegrityError
from django.shortcuts import redirect, render


from .forms import SignUpForm
from .models import CustomUser


# Create your views here.
def signup(request):
    """ Method for signing up a new user.
    """
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = CustomUser.objects.create_user(
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                )
                login(request, user)
                return redirect('mymainapp:wherenext')
            except IntegrityError:
                return render(request, 'users/signup.html', \
                              {'form': form, 'error': 'Email already exists'})
        else:
            return render(request, 'users/signup.html', {'form': form})
    else:
        return render(request, 'users/signup.html', {'form': form})
