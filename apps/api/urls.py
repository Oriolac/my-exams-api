from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from .views import *

API_TITLE = 'Exam API'
API_DESCRIPTION = 'A Web API for exams management'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('exam/<int:pk>/grades/<str:studentID>/', PutExamGrade.as_view()),
    path('exam/<int:pk>/grades/', ExamGrades.as_view()),
    path('exam/<int:pk>/desc/', UpdateDescriptionExamView.as_view()),
    path('exam/<int:pk>/<str:studentID>/', ExamAccess.as_view()),
    path('exam/<int:pk>/', ExamDetail.as_view()),
    path('exam/', ExamsList.as_view()),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('question/', QuestionList.as_view()),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
