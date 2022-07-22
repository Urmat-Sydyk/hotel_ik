from django.db import models

# Create your models here.
from backend.apps.accounts.models import User


class Rooms(models.Model):
    TYPE_LUX = 'Люкс'
    TYPE_JUNIOR = 'Полулюкс'
    TYPE_STANDART = 'Стандарт'
    TYPES = (
        (TYPE_LUX, 'Люкс'),
        (TYPE_JUNIOR, 'Полулюкс'),
        (TYPE_STANDART, 'Стандарт'),
    )
    type = models.CharField('Тип комнаты', max_length=20, choices=TYPES, default=TYPE_STANDART)
    number = models.CharField(max_length=50, verbose_name='Номер комнаты')

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return f'{self.type} - {self.number}'


class Booking(models.Model):
    guest_name = models.CharField(max_length=15, verbose_name='ФИО клиента')
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE, verbose_name='Комната')
    check_in = models.DateTimeField(verbose_name='Дата заезда')
    check_out = models.DateTimeField(verbose_name='Дата выезда')
    STATUS_RESERVE = 'Бронь'
    STATUS_LIVES = 'Проживает'
    STATUS_MOVED = 'Съехал'
    STATUSES = (
        (STATUS_RESERVE, 'Бронь'),
        (STATUS_LIVES, 'Проживает'),
        (STATUS_MOVED, 'Съехал'),
    )
    status = models.CharField('Статус', max_length=20, choices=STATUSES, default=STATUS_RESERVE)
    creater = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Сотрудник')

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return f'{self.guest_name} - {self.status}'
