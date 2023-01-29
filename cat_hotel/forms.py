from django import forms
from .models import Booking, Room, Customer

class BookingForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=Room.objects.all())
    start_date = forms.DateField(widget=forms.HiddenInput())
    start_time = forms.TimeField()
    end_date = forms.DateField()
    end_time = forms.TimeField()
    cat = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = Booking
        fields = [ 'room', 'start_date', 'start_time', 'end_date', 'end_time', 'cat', 'phone_number']