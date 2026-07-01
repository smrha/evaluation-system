from django.urls import path
from . import views

urlpatterns = [
    path('terms/', views.terms_list, name='term_list'),
    path('terms/create/', views.create_term, name='create_term'),
    path('terms/edit/<int:id>/', views.edit_term, name='edit_term'),
]
