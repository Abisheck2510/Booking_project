from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['passenger_name', 'age', 'gender', 'phone_number', 'pickup_point', 'drop_point', 'service_class']
