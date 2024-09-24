from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    Account = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Email = models.CharField(max_length=50, primary_key=True, verbose_name="Почта")


class Post(models.Model):
    Author = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    Title = models.CharField(max_length=100, verbose_name="Заголовок")
    Description = models.CharField(max_length=500, verbose_name="Описание")



