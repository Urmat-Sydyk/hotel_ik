from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, ListView, UpdateView

from backend.apps.accounts.forms import LoginForm, UserRegisterForm, UserUpdateForm
from backend.apps.accounts.models import User
from backend.apps.booking.models import Booking


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        pin = data['pin']
        password = data['password']
        user = authenticate(pin=pin, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('main')
            else:
                return HttpResponse("Ваш аккаунт неактивен")
        return HttpResponse("Такого юзера не существует")


def userRegister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created')
            return redirect('sign_in')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)


class UserProfilePage(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'user_profile.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        queryset = Booking.objects.all().order_by('room_id', 'check_in')
        return queryset


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('sign_in')


def main_page(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return redirect('sign_in')


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('profile')
    queryset = User.objects.all()
    model = User

    def test_func(self):    # проверка на совпадение айдишек залогиненного пользователя и айдишки с 'url'
        if self.kwargs.get('pk') == self.request.user.pk:
            return True
        return False


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('logout')
