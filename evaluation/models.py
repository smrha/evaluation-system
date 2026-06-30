from django.db import models
from django.contrib.auth.models import User


class Terms(models.Model):
    title = models.CharField(max_length=128, verbose_name='دوره ارزیابی')
    is_active = models.BooleanField(default=0 ,verbose_name='وضعیت')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    CATEGORY_CHOICES = (
        ('cat_1','شرایط حرفه ای کار'),
        ('cat_2', 'عوامل تخصصی')
    )

    title = models.TextField(verbose_name='سوال')
    order = models.IntegerField(default=1 ,verbose_name='شماره سوال')
    score_range = models.IntegerField(default=5 ,verbose_name='بازه امتیاز')
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICES, verbose_name='گروه سوال', default='cat_1')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    