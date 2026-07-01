from django.contrib import admin
from .models import Question, Terms, Exam, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'score_range', 'category']


@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['assessee', 'evaluator', 'term']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question_name', 'exam_name', 'value']

    def question_name(self, obj):
        return obj.question.title
    
    def exam_name(self, obj):
        return f'فرم ارزیابی {obj.exam.assessee.first_name} {obj.exam.assessee.last_name}'
    
    question_name.short_description = "عنوان سوال"
    exam_name.short_description = "دوره ارزیابی"