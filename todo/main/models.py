from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Заголовок задачи', max_length=200)
    description = models.TextField('Описание задачи')
    is_completed = models.BooleanField('Статус задачи',default=False)
    created_at = models.DateTimeField('Время создания задачи', auto_now_add=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title

