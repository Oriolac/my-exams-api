from rest_framework import generics, mixins, filters

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.serializers import *
from apps.exams.models import Exam, ExamLocation, Student, Question


class ExamsList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = Exam.objects.all()
    serializer_class = CompleteExamSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ExamAccess(APIView):

    def get(self, request, *args, **kwargs):
        exam: Exam = Exam.objects.get(pk=kwargs['pk'])
        try:
            student = exam.students.get(studentID=kwargs['studentID'])
            serializer = LocationSerializer(exam.location)
            return Response(serializer.data)
        except:
            return Response(status=401)


class ExamDetail(mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                 generics.GenericAPIView):
    queryset = Exam.objects.all()
    serializer_class = CompleteExamSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class LocationList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = ExamLocation.objects.all()
    serializer_class = LocationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LocationDetail(mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    queryset = ExamLocation.objects.all()
    serializer_class = LocationSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class QuestionList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class QuestionDetail(mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UpdateDescriptionExamView(generics.RetrieveUpdateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDescriptionSerializer


class ExamGrades(APIView):

    def get(self, request, *args, **kwargs):
        exam: Exam = Exam.objects.get(pk=kwargs['pk'])
        serializer = ExamGradesSerializer(exam.grade_set, many=True)
        return Response(serializer.data)


class PutExamGrade(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Grade.objects.all()
    serializer_class = CorrectExamGradesSerializer

    def get(self, request, *args, **kwargs):
        exam: Exam = Exam.objects.get(pk=kwargs['pk'])
        grade = exam.grade_set.get(student__studentID=kwargs['studentID'])
        serializer = ExamGradesSerializer(grade)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        exam: Exam = Exam.objects.get(pk=kwargs['pk'])
        grade = exam.grade_set.get(student__studentID=kwargs['studentID'])
        grade.correct = request.data['correct']
        grade.save()
        return Response(ExamGradesSerializer(grade).data)
