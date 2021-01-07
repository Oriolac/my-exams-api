from rest_framework import generics, mixins, filters

from django.http import HttpResponse

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
