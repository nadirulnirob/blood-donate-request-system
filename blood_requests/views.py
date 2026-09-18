from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import BloodRequest
from .forms import BloodRequestForm, BloodRequestCreateForm

def request_list(request):
    requests = BloodRequest.objects.all()

    blood_group = request.GET.get('blood_group')
    location = request.GET.get('location')
    status = request.GET.get('status')

    if blood_group:
        requests = requests.filter(blood_group=blood_group)

    if location:
        requests = requests.filter(
            hospital_location__icontains=location
        )

    if status:
        requests = requests.filter(status=status)

    paginator = Paginator(requests, 8)
    page = request.GET.get('page')
    requests = paginator.get_page(page)

    return render(request, 'blood_requests/request_list.html', {
        'requests': requests,
        'blood_group': blood_group,
        'location': location,
        'status': status
    })

def request_detail(request, pk):
    blood_request = get_object_or_404(BloodRequest, pk=pk)

    return render(request, 'blood_requests/request_detail.html', {
        'blood_request': blood_request
    })

@login_required
def request_create(request):
    if request.method == 'POST':
        form = BloodRequestCreateForm(request.POST)

        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.requester = request.user
            blood_request.status = 'Pending'
            blood_request.save()

            messages.success(
                request,
                'Blood request created successfully.'
            )

            return redirect(
                'request_detail',
                blood_request.pk
            )
    else:
        form = BloodRequestCreateForm()

    return render(request, 'blood_requests/request_form.html', {
        'form': form,
        'title': 'Request Blood'
    })

@login_required
def request_edit(request, pk):
    blood_request = get_object_or_404(BloodRequest, pk=pk)

    if blood_request.requester != request.user:
        messages.error(
            request,
            'You can only edit your own blood requests.'
        )
        return redirect('request_list')

    if request.method == 'POST':
        form = BloodRequestForm(
            request.POST,
            instance=blood_request
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Blood request updated successfully.'
            )
            return redirect(
                'request_detail',
                blood_request.pk
            )
    else:
        form = BloodRequestForm(instance=blood_request)

    return render(request, 'blood_requests/request_form.html', {
        'form': form,
        'title': 'Edit Blood Request'
    })

@login_required
def request_delete(request, pk):
    blood_request = get_object_or_404(BloodRequest, pk=pk)

    if blood_request.requester != request.user:
        messages.error(
            request,
            'You can only delete your own blood requests.'
        )
        return redirect('request_list')

    if request.method == 'POST':
        blood_request.delete()
        messages.success(
            request,
            'Blood request deleted successfully.'
        )
        return redirect('request_list')

    return render(
        request,
        'blood_requests/request_confirm_delete.html',
        {'blood_request': blood_request}
    )

@login_required
def my_requests(request):
    requests = BloodRequest.objects.filter(
        requester=request.user
    )

    paginator = Paginator(requests, 8)
    page = request.GET.get('page')
    requests = paginator.get_page(page)

    return render(request, 'blood_requests/my_requests.html', {
        'requests': requests
    })