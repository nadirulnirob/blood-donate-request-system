from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from donors.models import DonorProfile
from blood_requests.models import BloodRequest
from .forms import RegisterForm, ProfileForm, UserUpdateForm
from .models import UserProfile

def home(request):
    donors = DonorProfile.objects.filter(availability='Available').count()
    requests = BloodRequest.objects.filter(status='Pending').count()

    return render(request, 'home.html', {
        'donors': donors,
        'requests': requests
    })

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            UserProfile.objects.create(
                user=user,
                full_name=user.get_full_name(),
                phone='01700000000',
                blood_group='A+',
                location='Dhaka'
            )

            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    donor = DonorProfile.objects.filter(user=request.user).first()

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'donor': donor
    })

@login_required
def profile_edit(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
        user_form = UserUpdateForm(instance=request.user)

    return render(request, 'accounts/profile_edit.html', {
        'form': form,
        'user_form': user_form
    })