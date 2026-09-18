from django import forms
from django.utils import timezone
from .models import BloodRequest

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = [
            'patient_name',
            'blood_group',
            'hospital_name',
            'hospital_location',
            'required_date',
            'bags_required',
            'contact_number',
            'description',
            'status'
        ]
        widgets = {
            'required_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5})
        }

    def clean_required_date(self):
        date = self.cleaned_data['required_date']

        if date < timezone.localdate():
            raise forms.ValidationError(
                'Required date cannot be in the past.'
            )

        return date

    def clean_bags_required(self):
        bags = self.cleaned_data['bags_required']

        if bags <= 0:
            raise forms.ValidationError(
                'Number of bags must be positive.'
            )

        return bags

    def clean_contact_number(self):
        phone = self.cleaned_data['contact_number']

        if not phone.isdigit() or len(phone) != 11 or not phone.startswith(('013', '014', '015', '016', '017', '018', '019')):
            raise forms.ValidationError('Enter a valid Bangladesh phone number.')

        return phone


class BloodRequestCreateForm(BloodRequestForm):
    class Meta(BloodRequestForm.Meta):
        fields = [
            'patient_name',
            'blood_group',
            'hospital_name',
            'hospital_location',
            'required_date',
            'bags_required',
            'contact_number',
            'description'
        ]