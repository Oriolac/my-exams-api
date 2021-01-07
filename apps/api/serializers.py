from rest_framework import serializers

from apps.exams.models import Exam, ExamLocation, Question


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'title', 'description', 'date_start', 'date_finish', 'location')


class CompleteExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'title', 'description', 'date_start', 'date_finish', 'location', 'questions')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamLocation
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'choices', 'correct_choice')