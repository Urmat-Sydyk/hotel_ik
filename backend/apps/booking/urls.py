from django.urls import path, include

from backend.apps.accounts.views import LoginView, userRegister, UserProfilePage, user_logout, main_page, \
    UserUpdateView, UserPasswordChangeView
from backend.apps.booking.views import BookingCreateView

urlpatterns = [
    path('new/', BookingCreateView.as_view(), name='new_booking'),
]
