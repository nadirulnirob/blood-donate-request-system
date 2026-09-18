from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import DonorProfile
from .forms import DonorProfileForm

def donor_list(request):
    donors = DonorProfile.objects.all()

    blood_group = request.GET.get('blood_group')
    location = request.GET.get('location')
    availability = request.GET.get('availability')

    if blood_group:
        donors = donors.filter(blood_group=blood_group)

    if location:
        donors = donors.filter(location__icontains=location)

    if availability:
        donors = donors.filter(availability=availability)

    paginator = Paginator(donors, 9)
    page = request.GET.get('page')
    donors = paginator.get_page(page)

    return render(request, 'donors/donor_list.html', {
        'donors': donors,
        'blood_group': blood_group,
        'location': location,
        'availability': availability
    })

def donor_detail(request, pk):
    donor = get_object_or_404(DonorProfile, pk=pk)
    return render(request, 'donors/donor_detail.html', {'donor': donor})

@login_required
def donor_create(request):
    if DonorProfile.objects.filter(user=request.user).exists():
        messages.info(request, 'You already have a donor profile.')
        return redirect('profile')

    if request.method == 'POST':
        form = DonorProfileForm(request.POST, request.FILES)

        if form.is_valid():
            donor = form.save(commit=False)
            donor.user = request.user
            donor.save()

            messages.success(request, 'Donor profile created successfully.')
            return redirect('donor_detail', donor.pk)
    else:
        form = DonorProfileForm()

    return render(request, 'donors/donor_form.html', {
        'form': form,
        'title': 'Become a Donor'
    })

@login_required
def donor_edit(request, pk):
    donor = get_object_or_404(DonorProfile, pk=pk)

    if donor.user != request.user:
        messages.error(request, 'You can only edit your own donor profile.')
        return redirect('donor_list')

    if request.method == 'POST':
        form = DonorProfileForm(request.POST, request.FILES, instance=donor)

        if form.is_valid():
            form.save()
            messages.success(request, 'Donor profile updated successfully.')
            return redirect('donor_detail', donor.pk)
    else:
        form = DonorProfileForm(instance=donor)

    return render(request, 'donors/donor_form.html', {
        'form': form,
        'title': 'Edit Donor Profile'
    })

@login_required
def donor_delete(request, pk):
    donor = get_object_or_404(DonorProfile, pk=pk)

    if donor.user != request.user:
        messages.error(request, 'You can only delete your own donor profile.')
        return redirect('donor_list')

    if request.method == 'POST':
        donor.delete()
        messages.success(request, 'Donor profile deleted successfully.')
        return redirect('donor_list')

    return render(request, 'donors/donor_confirm_delete.html', {
        'donor': donor
    })