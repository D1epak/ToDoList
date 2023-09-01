from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'


class Task(models.Model):
    title = models.CharField('Название задачи', max_length=100)
    description = models.CharField('Описание задачи', max_length=100)
    user = models.ForeignKey(User, models.CASCADE, 'Пользователь')
    category = models.ForeignKey(Category, models.CASCADE, 'Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задача'
