from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm, UserProfileForm
from .models import UserProfile


def register_user(request):
    if request.method == 'POST':
        registration_form = SignUpForm(request.POST)
        login_form = LoginForm(request.POST)

        if registration_form.is_valid():
            user = registration_form.save()
            job_title = registration_form.cleaned_data['job_title']

            user_profile, created = UserProfile.objects.get_or_create(
                user=user)
            user_profile.job_title = job_title
            user_profile.save()

            auth_login(request, user)
            return redirect('members_list')

    else:
        registration_form = SignUpForm()
        login_form = LoginForm()

    return render(request, 'registration_login.html', {'registration_form': registration_form, 'login_form': login_form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        registration_form = SignUpForm()

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("members_list")
            else:
                messages.error(request, "Invalid username or password.")

    else:
        form = AuthenticationForm()
        registration_form = SignUpForm()

    return render(request, 'registration_login.html', {'login_form': form, 'registration_form': registration_form})


@login_required
def members_list(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'members_list.html', {'user_profiles': user_profiles})


@login_required
def profile_user(request):
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()

    else:
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'user_profile': user_profile, 'profile_form': profile_form})


@login_required
def profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user__id=user_id)
    return render(request, 'profile.html', {'user_profile': user_profile})


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')
