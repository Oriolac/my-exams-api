from django.urls import path

from .views import ListExams

urlpatterns = [
    path('', ListExams.as_view()),
]
