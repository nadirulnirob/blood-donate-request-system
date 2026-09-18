from django.contrib import admin
from .models import DonorProfile

@admin.register(DonorProfile)
class DonorProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'blood_group',
        'phone',
        'location',
        'availability',
        'last_donation_date'
    )
    list_filter = ('blood_group', 'availability', 'location')
    search_fields = ('user__username', 'user__first_name', 'phone', 'location')