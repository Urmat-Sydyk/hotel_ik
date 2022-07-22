from django.urls import path, include

from backend.apps.accounts.views import LoginView, userRegister, UserProfilePage, user_logout, main_page, \
    UserUpdateView, UserPasswordChangeView

urlpatterns = [
    path('', main_page, name='main'),
    path('profile/', UserProfilePage.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='sign_in'),
    path('register/', userRegister, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/change-password/', UserPasswordChangeView.as_view(), name='change_password')
]
