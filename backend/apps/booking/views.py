
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from backend.apps.accounts.models import User
from backend.apps.booking.forms import BookingCreateForm


class BookingCreateView(LoginRequiredMixin, CreateView):
    template_name = "create_booking.html"
    form_class = BookingCreateForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательна
        fields.creater = User.objects.get(id=self.request.user.id)
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)
