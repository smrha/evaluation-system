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

class Exam(models.Model):
    assessee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessees', verbose_name='ارزیابی شونده')
    evaluator = models.ForeignKey(User, models.CASCADE, related_name='evaloators',verbose_name='ارزیاب')
    term = models.ForeignKey(Terms, on_delete=models.CASCADE, verbose_name='دوره ارزیابی')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'فرم ارزیابی {self.assessee.first_name} {self.assessee.first_name}'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='سوال')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name='دوره ارزیابی')
    value = models.IntegerField(default=0, verbose_name='امتیاز')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

