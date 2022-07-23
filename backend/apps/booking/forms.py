from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from backend.apps.booking.models import Booking


class BookingCreateForm(forms.ModelForm):
    check_in = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input',
                                          'data-target': '#datetimepicker1'}))
    check_out = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input',
                                          'data-target': '#datetimepicker2'}))

    class Meta:
        model = Booking
        fields = [
            'room_id',
            'guest_name',
            'check_in',
            'check_out',
            'status',

        ]
        widgets = {
            'room_id': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Выберите комнату'}),
            'guest_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО клиента'}),
            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Статус'}),
        }


class BookingUpdateForm(forms.ModelForm):
    check_in = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input',
                                          'data-target': '#datetimepicker1'}))
    check_out = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input',
                                          'data-target': '#datetimepicker2'}))

    class Meta:
        model = Booking
        fields = [
            'room_id',
            'guest_name',
            'check_in',
            'check_out',
            'status',
        ]
        widgets = {
            'room_id': forms.Select(attrs={'class': 'form-control'}),
            'guest_name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
