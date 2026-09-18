from django.db import models
from django.contrib.auth.models import User
from accounts.models import BLOOD_GROUPS

class BloodRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Fulfilled', 'Fulfilled'),
        ('Cancelled', 'Cancelled'),
    ]

    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blood_requests'
    )
    patient_name = models.CharField(max_length=150)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    hospital_name = models.CharField(max_length=200)
    hospital_location = models.CharField(max_length=200)
    required_date = models.DateField()
    bags_required = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.patient_name} - {self.blood_group}'