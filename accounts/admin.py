from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'blood_group', 'phone', 'location')
    list_filter = ('blood_group', 'location')
    search_fields = ('full_name', 'phone', 'location')