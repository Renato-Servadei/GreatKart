from django.contrib import auth, messages
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from .models import Account

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            
            username = email.split('@')[0]
            user = Account.objects.create(first_name = first_name, last_name = last_name, email = email, username = username)
            user.phone_number = phone_number
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()
            messages.success(request, 'Registration successful')
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            #messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')

    return render(request, 'accounts/login.html')

def logout(request):
    return 