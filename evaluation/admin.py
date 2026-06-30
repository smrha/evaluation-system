from django.contrib import admin
from .models import Question, Terms

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'score_range', 'category']


@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']