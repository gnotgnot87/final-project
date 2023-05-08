from django import forms

from .models import Booking


class BookingForm(forms.ModelForm):
    name = forms.CharField(label="Your name")
    guests_count = forms.IntegerField(label="Guests count")
    booking_date = forms.DateField(
        input_formats=[
            "%Y-%m-%d",
        ],
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Date",
    )
    booking_slot = forms.IntegerField(label="Slot")

    class Meta:
        model = Booking
        fields = "__all__"
