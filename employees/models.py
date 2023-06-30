from django.db import models
from django.urls import reverse


class Productivity(models.Model):
    productivity = models.CharField(max_length=50)
    def __str__(self):
        return self.productivity


class Employees(models.Model):
    employe = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Выберите сотрудника'
    )
    work_time = models.TimeField(verbose_name='Введите время работы')
    productivity = models.ForeignKey(
        Productivity, 
        on_delete=models.CASCADE,
        verbose_name='Выберите продуктивность работника'
    )
    def __str__(self):
        return self.employe
    
    def get_absolute_url(self):
        return reverse('table')

    class Meta:
        verbose_name_plural = 'Сотрудники'