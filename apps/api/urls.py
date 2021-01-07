from django.urls import path

from .views import *

urlpatterns = [
    path('exam/<int:pk>/<str:studentID>', ExamAccess.as_view()),
    path('exam/<int:pk>/', ExamDetail.as_view()),
    path('exam/', ExamsList.as_view()),
    path('examdesc/<int:pk>/', UpdateDescriptionExamView.as_view()),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('question/', QuestionList.as_view()),
    path('question/<int:pk>/', QuestionDetail.as_view()),
]
