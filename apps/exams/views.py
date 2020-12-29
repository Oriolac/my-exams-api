from rest_framework import generics


from apps.api.serializers import CompleteExamSerializer
from apps.exams.models import Exam


# Create your views here.
class ListExamQuestions(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = CompleteExamSerializer

