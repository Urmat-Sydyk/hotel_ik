from django.urls import path, include

from backend.apps.accounts.views import LoginView, userRegister, UserProfilePage, user_logout, main_page, \
    UserUpdateView, UserPasswordChangeView
from backend.apps.booking.views import BookingCreateView, BookingUpdateView, BookingDeleteView

urlpatterns = [
    path('new/', BookingCreateView.as_view(), name='new_booking'),
    path('update/<int:pk>/', BookingUpdateView.as_view(), name='update_booking'),
    path('delete/<int:pk>/', BookingDeleteView.as_view(), name='delete_booking'),
]
