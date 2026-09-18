from django import forms
from .models import DonorProfile

class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields = [
            'blood_group',
            'phone',
            'location',
            'last_donation_date',
            'availability',
            'description',
            'profile_picture'
        ]
        widgets = {
            'last_donation_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4})
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if not phone.isdigit() or len(phone) != 11 or not phone.startswith(('013', '014', '015', '016', '017', '018', '019')):
            raise forms.ValidationError('Enter a valid Bangladesh phone number.')

        return phone