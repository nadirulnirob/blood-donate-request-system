from django.db import models
from django.contrib.auth.models import User
from accounts.models import BLOOD_GROUPS

class DonorProfile(models.Model):
    AVAILABILITY = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=150)
    last_donation_date = models.DateField(null=True, blank=True)
    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY,
        default='Available'
    )
    description = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='donors/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username