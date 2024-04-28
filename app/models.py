"""
Definition of models.
"""

from email.policy import default
from multiprocessing.spawn import old_main_modules
from tabnanny import verbose
from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib import admin #Добавили использование административного модуля
from django.urls import reverse
from django.contrib.auth.models import User

# Модель данных блога
class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    image = models.FileField(default = 'temp.jpg', verbose_name = 'Путь к картинке')

    def get_absolute_url(self):#Метод возвращает строку с уникальным интернет-адресом записи
        return reverse("blogpost", args=[str(self.id)])
    
    def __str__(self):#Метод возвращает название, используемое для предоставления отдельных записей
        return self.title
    
    class Meta:
        db_table = "Posts"
        ordering = ["-posted"]
        verbose_name = "Статья блога"
        verbose_name_plural = "Статьи блога"

admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = 'Дата')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья")
    
    def __str__(self):
        return 'Комментарий %s * %s' % (self.author, self.post)
    
    class Meta:
        db_table = "Comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий к статье блога"
        ordering = ["-date"]
        
admin.site.register(Comment)


