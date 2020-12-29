from rest_framework import generics

from django.http import HttpResponse

from apps.api.serializers import ExamSerializer
from apps.exams.models import Student
from apps.exams.models import Exam


# Create your views here.
def home_page_view(request):
    return HttpResponse('Hello' + Student.studentID + '!')


class ListExams(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class DetailExam(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


