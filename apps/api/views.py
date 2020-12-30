from rest_framework import generics

from django.http import HttpResponse

from apps.api.serializers import ExamSerializer, CompleteExamSerializer
from apps.exams.models import Student
from apps.exams.models import Exam


class ListExams(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class DetailExam(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ListExamQuestions(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = CompleteExamSerializer
