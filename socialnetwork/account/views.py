from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignupForm

User = get_user_model()


def signup_user(request):
    context = {}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.data['username']
            email = form.data['email']
            password = form.data['password']
            user = User.objects.create_user(email, username, password)
            login(request, user)
            return redirect('/home')
        else:
            context['errors'] = 'Email or Username incorrect'
    form = SignupForm()
    context['form'] = form
    return render(request, 'account/signup.html', context=context)


def login_user(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('/home')
        else:
            context['errors'] = "Erreur auhtentification"
    form = LoginForm()
    context['form'] = form
    return render(request, 'account/login.html', context=context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')
