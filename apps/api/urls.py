from django.urls import path

from .views import ExamsList, DetailExam

urlpatterns = [
    path('exams/', ExamsList.as_view()),
    path('exams/<int:pk>', DetailExam.as_view()),
]
