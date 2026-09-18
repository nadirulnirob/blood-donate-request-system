from django.contrib import admin
from .models import BloodRequest

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = (
        'patient_name',
        'blood_group',
        'hospital_name',
        'hospital_location',
        'required_date',
        'bags_required',
        'status',
        'requester'
    )
    list_filter = ('blood_group', 'status', 'hospital_location')
    search_fields = (
        'patient_name',
        'hospital_name',
        'hospital_location',
        'contact_number'
    )